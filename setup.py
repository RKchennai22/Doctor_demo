from setuptools import setup
from typing import List
   

#declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ramkumar"
DESCRIPTION="This is a first FSDS Nov  batch Machine laerning project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME='requirements.txt'


def get_requirements_list()->List[str]:
    """
    Description function is going to return list of requirements mention in requirements.txt.file

    return This function is going to return  a list which contain name of libraries  mentioned in requirement.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)
