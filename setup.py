from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    author='Amogh Ubhalkar',
    author_email='ubhalkar.amogh@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)