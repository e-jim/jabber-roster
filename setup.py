#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This a distutils script for creating distribution archives.
#
#   Copyright (C) 2010  Kamil Páral <kamil.paral /at/ gmail /dot/ com>
#  
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#  
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#  
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(name='xmpp-roster-migrater',
      version='0.1.2',
      py_modules=['xmpp_roster_migrater'],
      entry_points = {
        'console_scripts': ['xmpp-roster-migrater = xmpp_roster_migrater:main'],
      },
      install_requires=['xmpppy'],
      author='e-Jim',
      author_email='jim@e-jim.be',
      description='Tool for listing and exporting XMPP roster contacts',
      long_description='A simple Python tool for listing and exporting your XMPP roster contacts. You can use it to easily backup list of your buddies.',
      keywords='Jabber XMPP roster contacts commandline',
      license='GNU Affero GPL v3',
      url='https://github.com/e-jim/xmpp-roster-migrater',
      download_url='https://github.com/e-jim/xmpp-roster-migrater/downloads',
      classifiers=
        'Development Status :: 4  - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Utilities'
      ])
