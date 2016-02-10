import os
from distutils.core import setup

pts = dict(name=Blake,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=myproject,
            package_data=PACKAGE_DATA,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
