#!/usr/bin/env python3

from distutils.core import setup
from setuptools import find_packages

setup(name="pungen",
      version="1.0",
      author="Ennis Massey",
      author_email="ennisbaradine@gmail.com",
      description="A simple program to generate Punnet Squares from CLI",
      scripts=["bin/pungen"],
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: Python 3 :: Only",
          "Topic :: Scientific/Engineering",
          "Topic :: Utilities",
          "Environment :: Console",
          "Development Status :: 5 - Production/Stable"
      ])