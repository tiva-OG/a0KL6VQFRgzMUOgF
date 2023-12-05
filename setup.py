from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path):
    """
    this function will returns a list of requirements
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="a0KL6VQFRgzMUOgF",
    version="0.0.1",
    author="Tiva",
    author_email="tivasalvation@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
