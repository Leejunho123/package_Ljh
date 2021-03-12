import os
import io
from setuptools import find_packages, setup
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
    name='packageTest_Ljh',
    version="0.0.1",
    author="Leejunho123",
    author_email="naix123451@gmail.com",
    description="packageTesting",
    license='MIT',
    packages=find_packages(),
    keywords="Deep Learning",
    url="https://github.com/Leejunho123/package_Ljh",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False
)