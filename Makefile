install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,W0611 --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -cov=main test.py

all:
	install format test lint
