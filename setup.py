from setuptools import find_packages, setup 

setup(
	name='dragracer',
	version='0.1.0',
	author="Steven Miler, Zachary Brasseaux",
	author_email="zbrasseaux97@gmail.com",
	description="A Python port of an R package\
	containing data for RuPaul's Drag Race, Seasons\
	1-12. The package includes data at the episode-level,\
	contestant-level, and episode-contestant-level.", 
	platforms='Linux',
	packages=find_packages(where='./src'),
	package_dir={
		'': 'src'
	},
	include_package_data = True,
	install_requires=(
		'pandas',
	),
	classifiers=[
	'Development Status :: 1 - Alpha',
	'Natural Language :: English',
	'Programming Language :: Python',
	'Programming Language :: Python 3.5'
	],
	license='GPL-2'
)