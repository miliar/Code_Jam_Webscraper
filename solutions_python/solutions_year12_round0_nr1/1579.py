#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
rosetta = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
def translate(x):
	if(x == ' '): return ' '
        elif(x =='\n'): return ''
	else: return rosetta[ord(x)-ord('a')]

n = int(sys.stdin.readline())
for i in range(1,n+1):
	line = sys.stdin.readline()
	print 'Case #' + str(i) + ': ' + "".join(map(lambda x: translate(x), line))	
