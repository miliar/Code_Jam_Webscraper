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
		n = f.readline()
		n = int(n)

		chars = {
			'w': [1],
			'e': [2,7,15],
			'l': [3],
			'c': [4,12],
			'o': [5,10,13],
			'm': [6,19],
			' ': [8,11,16],
			't': [9],
			'd': [14],
			'j': [17],
			'a': [18]
		}

		for case in xrange(1, n+1):
			poses = [0]*20
			poses[0] = 1

			line = f.readline().strip()
			for char in line:
				if char in chars:
					for pos in chars[char]:
						poses[pos] += poses[pos-1]
			answer = poses[19]
			print "Case #%d: %04d" % (case, answer % 10000)
	return 0

if __name__ == '__main__': main()
