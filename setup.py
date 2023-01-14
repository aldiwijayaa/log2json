import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="log2json",
    version="0.0.4",
    author="M Aldi Wijaya",
    author_email="m.aldiwijaya97@gmail.com",
    description="Convert log to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
	entry_points={
		"console_scripts": [
			'log2json = log2json.__main__:main'
		]
	},
)
