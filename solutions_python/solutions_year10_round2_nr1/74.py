#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#
#       Copyright 2010 Denis <denis@sokolov.cc>
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

import os
import os.path

def solve(dirs, tbc):
	dirs.append('/')
	tbc.sort()
	result = 0
	for dir in tbc:
		if dir in dirs:
			continue
		result += 1
		dirs.append(dir)
		while not os.path.dirname(dir) in dirs:
			result += 1
			dir = os.path.dirname(dir)
			dirs.append(dir)
	return result

def main():
	for name in os.listdir('.'):
		if name.endswith('.in'):
			result = []
			with open(name) as f:
				for case in xrange(int(f.readline())):
					dirs = []
					n, m = map(int, f.readline().split(' '))
					for i in xrange(n):
						dirs.append(f.readline().strip())
					tbc = []
					for i in xrange(m):
						tbc.append(f.readline().strip())
					result.append('Case #%d: %d' % (case+1, solve(dirs, tbc)))
			with open('%s.out' % name, 'w') as f:
				f.write('\n'.join(result))
	return 0

if __name__ == '__main__':
	main()
