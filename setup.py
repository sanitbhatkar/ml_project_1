# Used for building our application as package

from setuptools import find_packages,setup
from typing import List

# Function for getting the requirements file
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        # Replacing escape character with blank space
        requirements = [req.replace("\n"," ") for req in requirements]

        # Removing the package builder

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# Setup file for building the packages

setup(

name = 'student_score_predictor',
version = '0.0.1',
author='Sanit',
author_email='sanitcoc@gmail.com',
packages= find_packages(),
install_requires=get_requirements('Requirements.txt')


)