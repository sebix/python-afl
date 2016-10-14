# encoding=UTF-8

# Copyright © 2014-2018 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
*python-afl* is an experimental module that enables
`American Fuzzy Lop`_ fork server and instrumentation for pure-Python code.

.. _American Fuzzy Lop: http://lcamtuf.coredump.cx/afl/
'''

import glob
import io
import os
import sys

from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = None

try:
    import distutils644
except ImportError:
    pass
else:
    distutils644.install()

b = b''  # Python >= 2.6 is required

def get_version():
    with io.open('doc/changelog', encoding='UTF-8') as file:
        line = file.readline()
    return line.split()[1].strip('()')

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: POSIX
Programming Language :: Cython
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
'''.strip().splitlines()

extensions = [
    Extension(
        "afl",
        ["afl.pyx"]
    ),
]

meta = dict(
    name='python-afl',
    version=get_version(),
    license='MIT',
    description='American Fuzzy Lop fork server and instrumentation for pure-Python code',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-afl',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    install_requires=['Cython>=0.19'],
    test_suite = 'nose.collector',
    ext_modules = cythonize(extensions),
)

setup(
    scripts=glob.glob('py-afl-*'),
    **meta
)

# vim:ts=4 sts=4 sw=4 et
