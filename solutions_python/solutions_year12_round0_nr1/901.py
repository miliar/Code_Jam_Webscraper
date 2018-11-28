#!/usr/bin/env python
# encoding: utf-8
"""
CODEJAM TEMPLATE

Created by Jamie Smith


"""

import sys
import os
from numpy import *
	
def readints(f):
	return map(int, f.readline().split())

def translate(s,d):
	s=list(s)
	s=map(lambda x: d[x], s)
	t=''
	for r in s:
		t=t+r
	return t

def main():
	os.chdir("/Users/Jamie/Documents/Codejam")
	
	# f=open('input.txt','r')
	g=open('googlerese.txt')
	f=open('A-small-attempt1.in','r')
	# f=open('A-large-practice.in','r')
	o=open('GooglereseOut.txt','w')
	
	T=int(f.readline())
	
	googlerese={}
	googlerese[' ']=' '
	googlerese['y']='a'
	googlerese['e']='o'
	googlerese['q']='z'
	googlerese['z']='q'
	
	
	
	
	for j in range(3):
		goo=list(g.readline().rstrip())
		eng=list(g.readline().rstrip())
		for k in range(len(goo)):
			googlerese[goo.pop(0)]=eng.pop(0)
			
	
	
	for j in range(T):
		s=f.readline().rstrip()
		result=translate(s,googlerese)
		
		
		
		
		# print "Case #%s: %s\n" % (j+1,result)
		o.write("Case #%s: %s\n" % (j+1,result))
	f.close()
	o.close()

if __name__ == '__main__':
	main()


