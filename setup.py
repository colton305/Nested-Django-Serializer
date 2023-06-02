from setuptools import setup

import nested_django_serializer.django.serializers

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="nested_django_serializer",
    version="1.1.0",
    author="Colton Schneider",
    description="Modifies the Django serializer such that it fully serializes foreign key relations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=(
        "nested_django_serializer",
        "nested_django_serializer.django",
        "nested_django_serializer.django.serializers"
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Framework :: Django"
    ],
    python_requires=">=3.8",
    install_requires=["django"],
    license="MIT",
    keywords="django json serializer",
    project_urls={
        "Github": "https://github.com/colton305/nested-django-serializer"
    }
)
