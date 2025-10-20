# run.py
import typer
from pyresolve.cli import create_app

if __name__ == "__main__":
    typer.run(create_app)