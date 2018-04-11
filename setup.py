from setuptools import setup

setup(  name='webSound',
        version='0.1',
        description='Web server to handle notification handle trigger sounds',
        author='Christophe TAPPRET',
        author_email="christophe.tappret@gmail.com",
        packages=['animator'],
        install_requires=[
            'flask',
            'flask_restful',
            'python-vlc'
        ],
        zip_safe=False)
