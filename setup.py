import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='pyramid_mako_starters',
    version='0.1.2',
    author='Ronan Amicel',
    author_email='ronan.amicel@gmail.com',
    url='https://github.com/ronnix/pyramid-mako-starters',
    description='Pyramid project scaffolds using Mako templates',
    long_description=README + '\n\n' + CHANGES,
    license='BSD',
    classifiers=[
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
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
