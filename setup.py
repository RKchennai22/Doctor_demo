from setuptools import find_packages, setup
from typing import List

#declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.6"
AUTHOR="Ramkumar"
DESCRIPTION="This is a first FSDS Nov  batch Machine laerning project"
HYPHEN_E_DOT = "-e ."
REQUIREMENTS_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    """
    Description function is going to return list of requirements mention in requirements.txt.file

    return This function is going to return  a list which contain name of libraries  mentioned in requirement.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=[requirement.replace("\n","") for requirement in requirement_file.readlines()]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
