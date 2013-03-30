from distutils.core import setup
# http://guide.python-distribute.org/creation.html

setup(
    name='serial_dumper',
    version='1.0.0',
    author='J. P. Petersen',
    author_email='joanpeturpetersen@gmail.com',
    packages=[],
    scripts=['serial_dumper.py'],
    url='https://github.com/JoanPeturPetersen/serial_dumper',
    license='MIT',
    description='Dump data from a serial port to standard out.',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial >= 2.6.0",
        "docopt >= 0.6.0",
    ],
)
