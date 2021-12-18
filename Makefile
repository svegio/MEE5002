PYTHON = python
POETRY = $(PYTHON) -m poetry
MKDOCS = $(POETRY) run mkdocs


.PHONY: serve build

serve:
	$(MKDOCS) serve

build:
	$(MKDOCS) build
