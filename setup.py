import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
    requirements = [x for x in requirements if not x.startswith("#") and x != ""]


setuptools.setup(
    name="pyflowqc", # Replace with your own username
    version="0.0.1",
    author="Simone Puccio",
    author_email="simone.puccio@cnr.it",
    description="PyFlowQC is a Python package for flow and mass cytometry quality control.",
#    long_description=long_description,
#    long_description_content_type="text/markdown",
    url="https://github.com/luglilab/pyflowqc",
    packages = setuptools.find_packages(),
    install_requires = requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)