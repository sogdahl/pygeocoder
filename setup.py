from setuptools import setup, find_packages
import pygeocoder

setup(
    name='pygeocoder',
    version=pygeocoder.__version__,
    description='API into the Google Maps geocoder.',
    long_description='\n'.join((
        open('README.md').read(),
        open('CHANGES.md').read(),
    )),
    author='Steven Ogdahl',
    author_email='steve.ogdahl@vanguardds.com',
    maintainer='Steven Ogdahl',
    url='https://github.com/sogdahl/pygeocoder',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"
    ],
    tests_require=[],
    include_package_data=True
)
