#!/usr/bin/env python
from setuptools import setup


setup(name='mani',
      version='0.3.2',
      packages=['mani'],
      install_requires=['redis',
                        'python-redis-lock',
                        'pytz'],
      setup_requires=['setuptools'],
      tests_require=['flake8'],
      description='Distributed cron',
      author='Sherin Kurian',
      author_email='sherinkurian.123@gmail.com',
      url='https://github.com/sherin/mani',
      download_url='https://github.com/sherin/mani/tarball/0.1',
      keywords=['cron', 'distributed', 'redis'],
      package_data={'mani.version': ['VERSION']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: Developers',
                   'Operating System :: Unix',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Topic :: System',
                   'Topic :: Software Development',
                   'Development Status :: 4 - Beta'])
