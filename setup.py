# setup.py

from setuptools import setup 

setup(
    name='site_checker',
    version='1.1',
    py_modules=[
        'site_checker',
    ],
    install_requires=[
        'click==8.1.7',
    ],
    entry_points={ 
        'console_scripts': [
            'check_site=site_checker:check_site',
        ]
        
    
        
    }
)