"""
Procedural map generator
"""
import os
import os.path
from setuptools import setup

# read the version number from the VERSION file
with open(os.path.join(os.getcwd(), 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name='mapgenerator',
    version=version,
    url='https://github.com/menzenski/map-generator',
    license='MIT',
    author='Matt Menzenski',
    author_email='matt.menzenski@gmail.com',
    description='Procedural map generator',
    long_description=__doc__,
    entry_points={
        'console_scripts': [
            'map-generator = map_generator.cli:main',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
)
