.PHONY: test install dev venv clean
.ONESHELL:

test:
	. .venv/bin/activate
	python3.11 -m unittest discover

install: venv
	. .venv/bin/activate
	python3.11 -m pip install -U pip setuptools wheel
	python3.11 -m pip install .

dev: venv
	. .venv/bin/activate
	python3.11 -m pip install -U pip setuptools wheel
	python3.11 -m pip install .[dev]
	pre-commit install

venv:
	test -d .venv || python3.11 -m venv .venv

clean:
	rm -r .venv
	find -iname "*.pyc" -delete
