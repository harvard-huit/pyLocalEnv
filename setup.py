from setuptools import setup, find_packages

setup(name='genLocalEnvFile',
      version='0.1',
      packages=find_packages(),
      install_requires=[
          'boto3',
          'pyyaml',
      ],
      scripts=['genLocalEnvFile']

      )
