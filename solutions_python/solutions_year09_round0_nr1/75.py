#!/usr/bin/env python
#
#       jam.py
#
#       Copyright 2009 Denis <denis@denis-desktop>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import re

def main():
	with open("in") as f:
		l, d, n = f.readline().split(' ')
		l = int(l)
		d = int(d)
		n = int(n)

		words = []
		for line in xrange(0,d):
			words.append(f.readline().strip())
		#words.sort()

		for case in xrange(1,n+1):
			pattern = f.readline().strip()
			pattern = pattern.replace('(','[').replace(')',']')
			test = re.compile(pattern)

			answer = 0
			for word in words:
				if test.match(word):
					answer += 1


			print "Case #%d: %s" % (case, answer)
	return 0

if __name__ == '__main__': main()
