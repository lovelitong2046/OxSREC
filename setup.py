from setuptools import setup

setup(
    name='ci_demo',

    version='0.1',

    description='Demonstration of setting up continuous integration for a Python project',

    license='MIT',

    packages=['ci_course'],

    install_requires=[
    ],

    extras_require={
        'docs': [
            'sphinx'
        ],
        'dev': [
            'flake8',
        ],
    },

    zip_safe=False
)
