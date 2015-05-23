from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='rakuten.ichiba',
      version=version,
      description="API for Rakuten Ichiba",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Maksym Shalenyi',
      author_email='maksym.shalenyi@gmail.com',
      url='',
      license='apache2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "furl",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
