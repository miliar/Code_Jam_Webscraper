# Google Code Jam 2012
# Pawel Przytula
# p.przytula@students.mimuw.edu.pl

import sys
def readline():
	s = sys.stdin.readline()
	return s.strip()

import string

trans = 'ynficwlbkuomxsevzpdrjgthaq'
t = string.maketrans(trans, string.ascii_lowercase)

if __name__ == "__main__":
	n = int(readline())
	for i in xrange(n):
		s = readline()
		print "Case #%s: %s" % (i + 1, s.translate(t)) 
