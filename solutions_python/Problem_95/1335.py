#!/usr/bin/python

import time, sys, os, string
start = time.clock()
print os.path.dirname(sys.argv[0])
sys.stdout = open(os.path.dirname(sys.argv[0]) + r'\output-a.txt', 'w')

f = open(sys.argv[1], 'r')
T = int(f.readline())

for i in xrange(T):
	line = f.readline()
	print 'Case #%d: %s' % (i + 1, line.translate(string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq')))
	
print >> sys.stderr, "%d us" % ((time.clock() - start) * 1000000)