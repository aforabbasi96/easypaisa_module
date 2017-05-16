from setuptools import setup

setup(
    name='easypaisapayment',
    version='1.0.1',
    packages=['migrations'],
    url='',
    license='MIT License',
    author='Qasim Gulzar',
    author_email='qasim.frt@gmail.com',
    description='',
    install_requires=['djangorestframework==3.6.3', 'markdown==2.6.8', 'psycopg2==2.7.1','django-filter==1.0.2'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
