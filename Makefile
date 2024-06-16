# Makefile

.PHONY: install test run

test:
	python -m unittest discover -s . -p "test_*.py"

run:
	python test-apka-python.py

