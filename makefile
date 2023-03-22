instal:
	poetry install

brain-games:
	poetry run python -m brain_games.scripts.brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl 