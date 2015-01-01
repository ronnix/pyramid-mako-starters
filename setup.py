import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='pyramid_mako_starters',
    version='0.1.1',
    author='Ronan Amicel',
    author_email='ronan.amicel@gmail.com',
    description='Pyramid project scaffolds using Mako templates',
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyramid',
    ],
    entry_points="""\
        [pyramid.scaffold]
        starter_mako=pyramid_mako_starters.scaffolds:StarterMakoTemplate
        alchemy_mako=pyramid_mako_starters.scaffolds:AlchemyMakoTemplate
    """,
)
