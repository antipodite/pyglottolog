import pathlib
from setuptools import setup, find_packages


setup(
    name='pyglottolog',
    version='3.8.0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='python package for glottolog data curation',
    long_description=pathlib.Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    keywords='data linguistics',
    license='Apache 2.0',
    url='https://github.com/clld/pyglottolog',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    platforms='any',
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'glottolog=pyglottolog.__main__:main',
            'glottolog-admin=pyglottolog.__main__:admin_main',
        ],
    },
    install_requires=[
        'gitpython',
        'pybtex>=0.22',
        'attrs>=19.2',
        'clldutils>=3.7',
        'cldfcatalog',
        'csvw>=1.5.6',
        'purl',
        'pycldf>=1.6.4',
        'sqlalchemy>=1.4',
        'tqdm',
        'latexcodec',
        'unidecode',
        'whoosh',
        'pycountry>=18.12.8',
        'termcolor',
        'newick>=0.9.2',
        'markdown',
        'requests',
        'nameparser',
        'linglit>=0.3',
        'cldfzenodo',
    ],
    extras_require={
        'dev': ['tox>=3.14', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['pytest>=5', 'pytest-mock', 'pytest-cov'],
        'docs': ['sphinx', 'sphinx-autodoc-typehints', 'sphinx-rtd-theme'],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
