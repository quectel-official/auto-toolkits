#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import re
import sys


if sys.version_info < (3, 6):
    sys.exit("Python 3.6 or newer is required.")

def find_text(key, file):
    return re.search(r"^{} = '(.*)'$".format(key),
                     open(file, 'r').read(),
                     re.MULTILINE).group(1)

def find_v2xpreconfig_cmd():
    return find_text('__cmd__', 'v2xpreconfig/v2xpreconfig.py')

setup(
    name='auto-toolkits',
    version='1.0.2',
    license='Apache License 2.0',
    packages=find_packages(),
    package_data={
        'v2xpreconfig': [
            '*.asn'
        ]
    },
    install_requires=[
        'asn1tools'
    ],
    entry_points={
        'console_scripts': [
            '{}=v2xpreconfig.__init__:main'.format(find_v2xpreconfig_cmd())
        ]
    }
)
