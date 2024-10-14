from setuptools import setup, find_packages
from typing import List


setup(
    name="Sensor",
    version="0.0.1",
    author="Manjunath",
    author_email="quora89@gmail.com",
    description="A brief description of your project",
    #long_description=open("README.md").read(),
    #long_description_content_type="text/markdown",
    #url="https://github.com/yourusername/Sensor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pymongo==4.2.0"
        # "pandas>=1.0.0",
    ],
)

