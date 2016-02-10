import os
from distutils.core import setup

opts = dict(name="Blake",
            description="my project for UWSEDS",
            packages=['myproject', 'myproject/tests'])


if __name__ == '__main__':
    setup(**opts)
