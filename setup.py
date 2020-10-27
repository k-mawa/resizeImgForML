from setuptools import setup, find_packages
import os

name = 'resizeImgForML'
version = '0.0.1'

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

def read_from_file(filename):
    return open(filename).read().splitlines()


short_description = '`resizeImgForML` is a package for resize images for machie learning.'


setup(
    name=name,
    version=version,
    url='https://github.com/k-mawa/resizeImgForML',
    description=short_description,
    long_description=readme,
    keywords=['machine', 'machine learning', 'resize', 'Pillow', 'PIL', 'openCV'],
    packages=find_packages(),
    install_requires=read_from_file('requirements.txt'),
    author='Kosuke Mawatari',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],

)