from setuptools import setup, find_packages
import os

# Helper function to include all files in 'model-last' directory
def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths

# Include all files in 'model-last' directory
model_files = package_files("model-last")

setup(
    name="mlops_finalproject",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": model_files},
    install_requires=[
        # Add your project dependencies here, e.g., transformers, torch, etc.
        "transformers",
        "torch"
    ],
    description="A resume parser project with pre-trained model",
)
