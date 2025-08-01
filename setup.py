'''
The setup.py file is an essential part of packaging and
distribution Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirement
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requiremets.txt file not found")
    
    return requirement_lst
print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    autohor="Deebyendu Mondal",
    author_email="bittupvm",
    packages=find_packages(),
    install_requires=get_requirements()
)

