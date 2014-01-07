from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-cf',
	version=version,
	description="N/A",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Athos Georgiou',
	author_email='N/A',
	url='N/A',
	license='N/A',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.cf'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.cf:PluginClass
	cf=ckanext.cf.plugin:ExampleIDatasetFormPlugin
	""",
)
