#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re

with open('snapshot/version.py', 'r') as version_file:
    version_match = re.search(r"^VERSION ?= ?['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)

with open("README.md", "r") as fh:
    long_description = fh.read()

if version_match:
    VERSION = version_match.group(1)
else:
    VERSION = '0.1'  #


setup(
    name='snapshot-cli',
    version=VERSION,
    description='Command line interface for create grafana snapshot by tags',
    long_description=long_description,
    keywords='grafana, snapshot, cli',
    author='Authapon Kongkaew',
    author_email='ohmrefresh@gmail.com',
    url='https://github.com/ohmrefresh/grafana-snapshot-cli',
    license="MIT",
    packages=find_packages(),
    install_requires=['grafana-snapshot'],
    tests_require=['tox', 'coverage', 'wheel', 'requests_mock', 'pytest'],
    py_modules=['snapshot-cli'],
    entry_points={
        'console_scripts': [
            'snapshot-cli=snapshot:main'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
