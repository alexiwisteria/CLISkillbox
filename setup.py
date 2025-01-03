# setup.py

from setuptools import setup, find_packages

setup(
    name="cliskillbox",  # Name of your package
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find all packages
    entry_points={
        "console_scripts": [
            "cliskillbox=cli_tool.main:main",  # CLI command and entry point
        ],
    },
    install_requires=[],  # Add dependencies if required
    description="A simple CLI tool for managing a to-do list",
    author="Alex Wisteria",  # Replace with your name
    author_email="alex@example.com",  # Replace with your email
    url="https://github.com/alexiwisteria/CLISkillbox",  # Replace with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version
)
