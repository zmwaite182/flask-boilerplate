Make directory and move into it
Initialize git directory
Add .gitignore
Add setup.py (change name and version)(add extras_require dict)
Make virtual environment
Start virtual environment and run which python to test
Run pip install -e . (to install things within install_requires) and use which to test
Run pip install -e '.[test]' (to install test within extras_require) and use which to test
Add bash variables with export FLASK_APP="app name"/FLASK_ENV="developer"
Make package directory
Make __init__.py within package directory
	Within __init__.py:
	import Flask class
	add create_app function
	create app as instance of Flask class
	add index function with default URL decorator
	in index function return 'Hello World'
	return app from create_app function

Run app
