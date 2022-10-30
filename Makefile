# Link for reference: https://makefiletutorial.com/

update-reqs:
	poetry update

all-tests:
	tox -r
	coverage xml -i
	coverage html -i