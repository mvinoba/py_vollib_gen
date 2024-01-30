#!/usr/bin/env python
# encoding: utf-8


from setuptools import setup, find_packages


setup(
    name='py_vollib_gen',
    version='1.0.1',
    description='',
    url='',
    maintainer='',
    maintainer_email='',
    long_description=open('README.rst').read(),
    license='MIT',
    install_requires=[
        'py_lets_be_rational_gen',
        'simplejson',
        'numpy',
        'pandas',
        'scipy'
    ],
    packages=find_packages()
)
