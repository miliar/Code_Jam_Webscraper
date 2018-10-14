#!/usr/bin/python

import sys

googish = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
english = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

transkey = {}

spot = 0
for character in googish:
	if (character != ' '):
		transkey[character] = english[spot]
		#print "character: %s" % (character)
		#print "equals:    %s" % transkey[character]

	spot += 1

transkey[' '] = ' '
transkey['\n'] = '\n'
transkey['z'] = 'q'
transkey['q'] = 'z'

infile = open("A-small-attempt1.in")

numcases = infile.readline()

for i in range(int(numcases)):
	print "Case #%i: " % (i + 1),
	line = infile.readline()
	for character in line:
		sys.stdout.write(transkey[character])




