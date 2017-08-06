"""
Procedural map generator
"""
import os
import os.path
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "map_generator", "__about__.py")) as about_file:
    exec(about_file.read(), about)

setup(
    name='mapgenerator',
    version=about['__version__'],
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
