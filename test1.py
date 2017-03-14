#!/usr/bin/env python
""" Test file for github
    by Minh Chau
"""

while True:
    name = raw_input("What's your name? ")
    if not name.isalpha():
	    print 'Please try again.'
    else:
        break

while True:
    number = raw_input('How tall are you in inches? ')
    try:
        height = float(number)
    except ValueError:
        print "'" + number + "'" + " is not a number! Please try again."
    else:
        break

if height > 72:
    print "%s, " % name + "you are %.1f feet which is tall." % (height/12)
elif height > 60 and height <= 72:
    print "%s, " % name + "you are %.1f feet which is medium." % (height/12)
else:
    print "%s, " % name + "you are %.1f feet which is short." % (height/12)


