from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='geometool',
    version='0.0.1',
    packages=['geometool'],
    install_requires=[
        'math'
        'abc'
    ],
    author='Idris Taha',
    author_email='dri.taha24@gmail.com',
    description='A Geometric Shape Calculator Tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/K4speeer/Geometry_Tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)