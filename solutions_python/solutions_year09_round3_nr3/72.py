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

#import re
import itertools

tor = []
p = 0
q = 0
def solve(left, right):
	global tor
	if not tor:
		return 0
	if left > right:
		return 0

	i = 0
	middle = float(right + left)/float(2)
	'''
	goon = True
	l = len(tor)
	while goon:
		if i >= l:
			goon = False
			i -= 1
		if tor[i] > middle:
			goon = False
		i += 1
	i -= 1
	if i > 0 and abs(middle - tor[i-1]) <= abs(middle - tor[i]) and tor[i-1] >= left:
		i -= 1
	'''
	min = {'diff': 99999, 'pos': -1}

	for i in xrange(0,len(tor)):
		newdiff = abs(middle-tor[i])
		if newdiff < min['diff']:
			min['diff'] = newdiff
			min['pos'] = i

	released = tor[min['pos']]
	if released < left or released > right:
		return 0
	#print left,' ',middle,' ',right
	#print 'of',tor,'choose',released
	del tor[min['pos']]
	answer = right-left
	answer += solve(left, released-1)
	answer += solve(released+1, right)
	return answer

def force(to, left, right):
	aaa = 99999
	if not to:
		return 0
	if left == right:
		return 0
	i = 0
	#print 'Got',to,left,right

	l = len(to)
	while i < l and to[i] < left:
		i += 1
	#print 'Skipped to',i,'(',to[i],')'

	while i < l and to[i] <= right:
		answer = right-left
		if i > 0:
			answer += force(to[:i], left, to[i]-1)
		if i < l:
			answer += force(to[i+1:], to[i]+1, right)
		aaa = min(aaa, answer)
		i += 1

	return aaa



def main():
	global tor, p, q
	with open("C-small-attempt5.in") as f:
		n = f.readline()
		n = int(n)


		for case in xrange(1, n+1):
			p, q = map(int, f.readline().strip().split(' '))
			tor = map(int, f.readline().strip().split(' '))

			#answer = solve(1, p)
			answer = force(tor, 1, p)
			print "Case #%d: %d" % (case, answer)
	return 0

if __name__ == '__main__': main()