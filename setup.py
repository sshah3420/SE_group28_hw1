from setuptools import setup

setup(
   name='calc_basic',
   version='1.0',
   description='hw1',
   author='CSC510 students',
   author_email='sshah35@ncsu.edu',
   packages=['foo'],  #same as name
   install_requires=['pytest', 'atomicwrites','attrs', 'colorama', 'iniconfig', 'packaging', 'pluggy','pypyparsing','tomli'] #external packages as dependencies
)