#coding: utf-8
#! /usr/bin/env python2.7

import sys


def solver(r, t):
	i = 0
	sum = 0
	while 1:
		sum += (4*(i+1) + 2*r -3)
		if sum > t:
			return i
		else: 
			i += 1

def main():
	line = []
	for l in sys.stdin: line.append(l[:-1])
	
	counter = 0
	num = int(line[counter])
	counter += 1

	for i in range(num):
		r, t = line[counter].split(' ')[0], line[counter].split(' ')[1]
		ans = solver(int(r), int(t))
		counter += 1

		print 'Case #%d: %d' % (i+1, ans)

if __name__ == '__main__':
	main()
