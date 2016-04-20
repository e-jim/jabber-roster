xmpp-roster-migrater
=============

A simple Python tool for listing your XMPP roster contacts and export it to another account. You can use it to easily backup list of your buddies.

This program is in development and no warranty can be made about it. Run it at your own risks.

It is licensed under GPL 3.

It is a fork from Kamil Páral's jabber-roster (https://github.com/kparal/jabber-roster) which is licensed under AGPL license as well.

Note that AGPL license permits the conveying of a derivative program under GPL3 as done in this case, but both GPL and AGPL licenses stress that the special requirements of AGPL concerning interaction through a network are still applicable to the new program. (Art. 13 of the AGPL and art. 13 of the GPL)

Running
=======

You can run the tool directly simply by:

    $ ./xmpp_roster_migrater.py

or by:

    $ python xmpp_roster_migrater.py

(use `--help` option of course if you don't know this tool yet)


Installation
============

For now on, it is only possible to install it through git on github/framagit.
To install, type 'git clone https://framagit.org/e-Jim/xmpp-roster-migrater'




Dependencies
============

If you haven't used the recommended way of installation, you might need to manually install some dependencies:

 * xmpppy: <http://xmpppy.sourceforge.net/> (usually available as `python-xmpp` package)

**PLEASE NOTE**: Currently it is necessary to install `xmpppy` from a forked
project <https://github.com/ArchipelProject/xmpppy> instead of the official
upstream project, because it does not contain
[a fix for latest SSL changes](https://github.com/ArchipelProject/xmpppy/commit/c61c64972b12d3bfeca7200a18965886cbf51263).
Once it is updated (if it is), you can go back to using original `xmpppy`.


License
=======

This program is a free software, licensed under GNU GPL 3, although previous work (jabber-roster) is licensed under AGPL3.
See `LICENSE` file.


Donations
=========

If you like this program you can [Flattr the author of jabber-roster on whose job I relied](https://flattr.com/thing/78799/jabber-roster).
We all are dwarves on other dwarves elbows. There is no giant.

[![](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/thing/78799/jabber-roster)


Contact
=======

Visit program homepage at: <https://framagit.org/e-Jim/xmpp-roster-migrater>

Please report all bugs to the [issue tracker](https://framagit.org/e-Jim/xmpp-roster-migrater/issues), but don't request new features unless you have a patch for it. This is a small personal project and I don't plan to spend much more time on it. I will gladly merge your patches if they look reasonable.
