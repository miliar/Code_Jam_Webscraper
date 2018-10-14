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

def solve(xs, vs, b, k, t, n):
	xs.reverse()
	xs = [(b-i) for i in xs]
	vs.reverse()
	i = 0
	swaps = 0
	while k > 0 and i < n:
		if (t*vs[i] >= xs[i]):
			k -= 1
		else:
			swaps += k
		i += 1
	if k > 0:
		return 'IMPOSSIBLE'
	return swaps

def main():
	for name in os.listdir('.'):
		if name.endswith('.in'):
			result = []
			with open(name) as f:
				for case in xrange(int(f.readline())):
					dirs = []
					n, k, b, t = map(int, f.readline().split(' '))
					xs = map(int, f.readline().split(' '))
					vs = map(int, f.readline().split(' '))
					result.append('Case #%d: %s' % (case+1, solve(xs, vs, b, k, t, n)))
			with open('%s.out' % name, 'w') as f:
				f.write('\n'.join(result))
	return 0

if __name__ == '__main__':
	main()
