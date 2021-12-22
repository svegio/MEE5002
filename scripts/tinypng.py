import os
import shutil
import subprocess
import tempfile


def tinypng(input_path: str, output_path: str) -> bool:
    '''
    - Argument:
        - input_path: 输入路径
        - output_path: 输出路径
    '''
    if not os.path.exists(input_path):
        return False
    with tempfile.NamedTemporaryFile(
        suffix=os.path.splitext(input_path)[-1], delete=False
    ) as f:
        for command in (
            (

                'ffmpeg', '-i', input_path,

                '-vf', 'palettegen=max_colors=256:stats_mode=single',

                '-y', f.name,

            ), (

                'ffmpeg', '-i', input_path, '-i', f.name,

                '-lavfi', '[0][1:v] paletteuse', '-pix_fmt', 'pal8',

                '-y', output_path,

            )
        ):
            subprocess.run(command)
    os.unlink(f.name)
    if os.path.exists(output_path):
        if os.path.getsize(output_path) > os.path.getsize(input_path):
            shutil.copy(input_path, output_path)  # 未起到压缩目的
    else:
        shutil.copy(input_path, output_path)  # 压缩失败
    return True
