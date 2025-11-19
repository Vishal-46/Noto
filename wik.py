import requests
import pandas as pd

# Example of using Poetry for Python package management

# First, initialize a new project:
# poetry new my-project
# or in existing directory:
# poetry init

# Install dependencies
# poetry add requests pandas numpy
# poetry add pytest --group dev
"""
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"
pandas = "^1.5.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
flake8 = "^5.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""

# Common Poetry commands:
# poetry install          # Install dependencies
# poetry shell            # Activate virtual environment
# poetry run python app.py   # Run script in poetry env
# poetry add package-name     # Add new dependency
# poetry remove package-name  # Remove dependency
# poetry update              # Update dependencies
# poetry build               # Build package
# poetry publish             # Publish to PyPI

# Example main application

def main():
    """Example function using installed dependencies"""
    response = requests.get("https://api.github.com")
    data = response.json()
    df = pd.DataFrame([data])
    print(df.head())

if __name__ == "__main__":
    main()