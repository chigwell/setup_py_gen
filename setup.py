from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='setup_py_gen',
    version='2025.9.81452',
    description='A package generated from provided source code and metadata.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='hi@eugene.plus',
    url='https://github.com/chigwell/setup_py_gen',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
