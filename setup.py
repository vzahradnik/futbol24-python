from setuptools import setup, find_packages

setup(name='futbol24-python',
      version='0.1',
      description='Unofficial Python API for Futbol24.com',
      url='https://github.com/vzahradnik/futbol24-python',
      author='Vladimir Zahradnik',
      author_email='vladimir.zahradnik@gmail.com',
      license='Apache License 2.0',
      packages=find_packages(),
      install_requires=[
          'requests',
          'lxml',
          'dateutils'
      ],
      zip_safe=False)
