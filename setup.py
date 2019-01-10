

from setuptools import setup, find_packages

setup(name='cbpi-httpsensor',
      version='4.0.0',
      description='CraftBeerPi Http Sensor',
      author='Manuel Fritsch',
      author_email='manuel@craftbeerpi.com',
      url='http://web.craftbeerpi.com',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi-httpsensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi-httpsensor'],
     )



