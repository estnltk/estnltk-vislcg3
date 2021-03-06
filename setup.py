# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
import os
import sys

os.environ['CC'] = 'g++'
os.environ['CXX'] = 'g++'


def get_sources(src_dir='src', ending='.cpp'):
    """Function to get a list of files ending with `ending` in `src_dir`."""
    return [os.path.join(src_dir, fnm) for fnm in os.listdir(src_dir) if fnm.endswith(ending)]

#lib_sources = get_sources()
swig_interface = os.path.join('estnltk_vislcg3', 'vislcg3.i')
swig_opts = ['-builtin']
#lib_sources.remove(os.path.join('src', 'icu_uoptions.cpp'))
lib_sources = [os.path.join('src', 'all_vislcg3.cpp')]

# Python 3 specific configuration
extra = {}
if sys.version_info[0] == 3:
    swig_opts.append('-py3')
swig_opts.append('-c++')

setup(
    name = "estnltk_vislcg3",
    version = "1.3",

    packages = find_packages(),
    include_package_data=True,

    author       = "University of Tartu",
    license      = "GPLv3",
    url          = "https://github.com/estnltk",
    ext_modules = [
        Extension('estnltk_vislcg3._vislcg3',
                  [swig_interface] + lib_sources,
                  swig_opts = swig_opts,
                  include_dirs=['src', 'include',
                                os.path.join('include', 'posix'),
                                os.path.join('include', 'win32'),
                                os.path.join('include', 'boost')])
        ],

    install_requires = ['estnltk==1.3'],

    classifiers = ['Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Information Technology',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Text Processing',
                   'Topic :: Text Processing :: Linguistic']
)
