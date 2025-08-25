from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version = '0.0.0',
    author = 'Mohit Vyas',
    author_email = 'MohitVyas1685@Gmail.Com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)