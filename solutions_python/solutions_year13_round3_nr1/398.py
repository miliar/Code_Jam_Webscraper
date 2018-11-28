#!/usr/bin/env pypy
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011–2013 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Consonants
"""

from string import lowercase
vowels = "aeiou"
#consonants = set(lowercase) - vowels

def score(s, n):
	s = s.split()
	return 1 if any(len(u) >= n for u in s) else 0

def n_value(name, n):
	l = len(name)
	s = 0
	for v in vowels:
		name = name.replace(v, " ")
	for b in range(l-n+1):
		for e in range(b+n, l+1):
			s += score(name[b:e], n)
	return s

T = ni(); nl();
for X in xrange(T):
 	print "Case #%s:" % (X+1),
	name, n = nt(), ni()
	nl()
	print n_value(name, n)