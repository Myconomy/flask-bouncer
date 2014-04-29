#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('flask_bouncer/__init__.py'))

def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


def strip_comments(l):
    return l.split('#', 1)[0].strip()

def desc():
    info = read('README.rst')
    try:
        return info + '\n\n' + read('CHANGES.rst').replace('.. :changelog:', '')
    except IOError:
        return info

def reqs(*f):
    return [
        r for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]

install_requires = reqs('requirements.txt')
tests_require = reqs('requirements-test.txt')

setup(
    name='flask-bouncer',
    version=grep('__version__'),
    license=grep('__license__'),
    author=grep('__author__'),
    author_email=grep('__email__'),
    description='Flask Simple Declarative Authentication based on Ryan Bates excellent cancan library',
    long_description=desc(),
    url='http://github.com/jtushman/flask-bouncer',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    zip_safe=False,
    keywords='bouncer',
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
