import os
from setuptools import setup
import codecs

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

requirements = [
    "numpy",
    "biopython",
    "freesasa"
]

setup(
    name='prodigy',
    version = "2.1.0",
    description=("PROtein binDIng enerGY prediction."),
    url='http://github.com/haddocking/prodigy',
    author='Computational Structural Biology Group @ Utrecht University',
    author_email='prodigy.bonvinlab@gmail.com',
    license='Apache 2.0',
    packages=['prodigy', 'prodigy.lib'],
    package_dir={'prodigy': 'prodigy'},
    package_data={'prodigy':['naccess.config',]},
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'prodigy = prodigy.predict_IC:main',
        ]
    },
    zip_safe=True
)
