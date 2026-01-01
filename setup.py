from setuptools import find_packages,setup

def get_requirements(file_path):
    requirements=[]
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name="MLproject",
    version='0.0.1',
    author='honey',
    author_email='honeychoudhary9797@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)