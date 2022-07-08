#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='hotmart-developers-python',
      version='0.2',
      description='Hotmart Developers requests made easy',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Bruno Armanelli',
      author_email='brunoarmanelli@me.com',
      url='https://github.com/brunoarmanelli/hotmart-developers-python',
      packages=['hotmart'],
      keywords='hotmart developers',
      install_requires=['requests', 'six']
     )