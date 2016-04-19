#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A small Python tool for listing your Jabber roster contacts. You can use it 
# to easily backup list of your buddies.
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


#
#   Work in progress par e-Jim sous la même licence.
#

import sys, getpass, locale, warnings
from optparse import OptionParser
# ignore deprecation warnings coming from xmpp, we can't do anything about it
warnings.filterwarnings(action='ignore', category=DeprecationWarning, module='xmpp')
import xmpp

# set user's default locale
locale.setlocale(locale.LC_ALL, '')

version = '0.1.2.0'

def main_run():
    '''Execute the whole program'''

    usage = '''Usage: %prog <server> <login> [<second server> <second login>]
Example: %prog jabber.org john.doe
If a second server is set, the roster from the first server will be migrated to the second one.
Program will output sorted list of roster contacts in form of "Alias: JID [Groups]"'''

    parser = OptionParser(usage=usage, version=version)
    parser.add_option('--debug', action='store_true', default=False,
                      help='Print debugging messages')
    (opts, args) = parser.parse_args()

    if len(args) < 2:
        parser.error("Insufficient number of arguments")

    server = args[0]
    login = args[1]

    client = xmpp.Client(server, debug='always' if opts.debug else None)
    client.connect()

    if not client.isConnected():
        print >> sys.stderr, "Could not connect to %s" % server
        sys.exit(1)

    try:
        #password = raw_input("Enter your password: ")
        password = getpass.getpass('Enter your password: ')

        auth = client.auth(user=login, password=password, resource='jabber-roster-export')
        if not auth:
            print >> sys.stderr, "Authentication failed"
            sys.exit(2)

        roster = client.getRoster()
        jids = roster.getItems()

        output = []
        contact_list = []

        for jid in jids:
            name = roster.getName(jid)
            groups = roster.getGroups(jid)
            if groups is None:
                groups = ['Default']
            line = u'%s: %s [%s]' % (name or '', jid, ', '.join(groups) if groups else '')
            output.append(line)
            contact_list.append([jid,name,groups])
        output.sort(cmp=locale.strcoll)

        for line in output:
            # "print line" would be easier, but redirection of unicode strings into
            # a file is currently broken. See http://bugs.python.org/issue4947
            sys.stdout.write(line.encode('UTF-8') + '\n')

    finally:
        client.disconnect()

    if len(args)== 4 :

        login_destination = args[3]
        server_destination = args[2]
        client_destination = xmpp.Client(server_destination, debug='always' if opts.debug else None)
        client_destination.connect()
    
        if not client_destination.isConnected():
            print >> sys.stderr, "Could not connect to %s" % server_destination
            sys.exit(1)

        try:
            password_destination = getpass.getpass('Enter your password for destination server: ')

            auth = client_destination.auth(user=login_destination, password=password_destination, resource='jabber-roster-import')
            if not auth:
                print >> sys.stderr, "Authentication failed on server %s" % server_destination
                sys.exit(2)

            roster_destination = client_destination.getRoster()

            for contact in contact_list:

                print contact            
                roster_destination.setItem(contact[0],contact[1],contact[2])
            


        finally:
            client_destination.disconnect()

def main():
    '''Main program entry point'''
    try:
        main_run()
    except KeyboardInterrupt:
        print 'Interrupted, exiting...'
        sys.exit(1)


if __name__ == '__main__':
    main()

