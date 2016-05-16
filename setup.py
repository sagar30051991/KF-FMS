# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='fms',
    version=version,
    description='Facility Management System',
    author='New Indictrans Technology Pvt Ltd',
    author_email='sagar.s@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
