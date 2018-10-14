#!/usr/bin/python

#          abcdefghijklmnopqrstuvwxyz
mapping = "yhesocvxduiglbkrztnwjpfmaq"

n = int(raw_input().strip())

def replace(x):
	if 'a' <= x <= 'z':
		return mapping[ord(x) - ord('a')]
	else:
		return x

for i in xrange(n):
	print "Case #%d: %s" % (i + 1, "".join([replace(x) for x in raw_input().strip()]))

