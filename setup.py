from os.path import join, dirname

import math_mind
from setuptools import setup, find_packages

setup(
        name="math_mind",
        # в __init__ пакета
        version=math_mind.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['mmind = math_mind.main:Main']
        }

)

