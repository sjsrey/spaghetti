"""Spatial Network Analysis (SPAtial GrapHs: nETworks, Topology, & Inference
"""

from setuptools import setup
from distutils.command.build_py import build_py

# Get __version__ from PACKAGE_NAME/__init__.py without importing the package
# __version__ has to be defined in the first line
with open('spaghetti/__init__.py', 'r') as f:
    exec(f.readline())

def _get_requirements_from_files(groups_files):
    groups_reqlist = {}
    for k,v in groups_files.items():
        with open(v, 'r') as f:
            pkg_list = f.read().splitlines()
        groups_reqlist[k] = pkg_list
    return groups_reqlist

def setup_package():
    package = 'spaghetti'
    
    _groups_files = {
        'base': 'requirements.txt', #basic requirements
        'tests': 'requirements_tests.txt', #requirements for tests
        'docs': 'requirements_docs.txt' #requirements for building docs
    }
    reqs = _get_requirements_from_files(_groups_files)
    install_reqs = reqs.pop('base')
    extras_reqs = reqs

    setup(name=package, #name of package
          version=__version__,
          description=__doc__, #short <80chr description
          url='https://github.com/pysal/spaghetti', #github repo
          maintainer='James Gaboardi',
          maintainer_email='jgaboardi@gmail.com',
          test_suite = 'nose.collector',
          tests_require=['nose'],
          keywords='spatial statistics, networks, graphs',
          classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: GIS',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
            ],
          license='3-Clause BSD',
          packages=[package], #add your package name here as a string
          install_requires=install_reqs,
          extras_require=extras_reqs,
          zip_safe=False,
          cmdclass = {'build.py':build_py})

if __name__ == '__main__':
    setup_package()