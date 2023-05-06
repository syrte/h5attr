from setuptools import setup

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='h5attr',
    version='0.9',
    description="H5Attr: Quick access to hdf5 data via attributes, allowing `group.key` instead of `group['key']` and IPython/Jupyter tab completion.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/syrte/h5attr/',
    keywords=['Fortran', 'Numpy'],
    author='Syrtis Major',
    author_email='styr.py@gmail.com',
    py_modules=['h5attr'],
    install_requires=['h5py', 'numpy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
