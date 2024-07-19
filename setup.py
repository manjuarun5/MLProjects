from setuptools import setup, find_packages
from typing import List

HYPHEN_EDOT = "-e."
def get_requirements(file_path:str) -> list[str]:
    '''
    retrun the list of requirements from the file
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if(HYPHEN_EDOT in requirements):
            requirements.remove(HYPHEN_EDOT)

setup(
    name='vava',
    version='1.0',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
    author='Manju',
    author_email='manju.arun.anjiliparambil@gmail.com',
    description='ML Project',
    url='https://github.com/manjuarun5/MLProjects',
)