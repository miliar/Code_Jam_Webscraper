#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

def main():

	f = sys.stdin
	
	cases = int(f.readline())
	for case in range(1, cases+1):
		tmp = [int(x) for x in f.readline().split(' ')]
		letter_per_key = tmp[0]
		keys = tmp[1]
		letters = tmp[2]
		
		data = [int(x) for x in f.readline().split(' ')]
		data.sort()
		data.reverse()
		
		press = 1
		result = 0
		i = 0
		for count in data: 
			result = result + count*press
			i = i+1
			if i >= keys:
				i = 0
				press = press+1
				
		if press > letter_per_key+1:
			result = "impossible"	
		else:
			result = str(result)
	
		print "Case #%(case)d: %(result)s" % locals()
		
	
if __name__ == '__main__':
	sys.exit(main())


