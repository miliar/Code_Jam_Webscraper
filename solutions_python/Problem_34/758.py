#!/usr/bin/python
import re
f=open('input.txt')
length,dict,test = f.readline().split()
length,dict,test = int(length), int( dict), int( test)
words = list()
tests = list()
for i in range(0, dict):
	words.append(f.readline())
for i in range(0, test):
	tests.append(f.readline().replace('(', '[').replace(')',']'))

def asbdafh(x):
	if(x == None): return 0
	return 1

i=0
for t in tests:
	r = re.compile(t)
	i+=1
	print "Case #%d: %d" % (i,reduce(lambda x,y: x+y, map(asbdafh, map(r.match, words))))


#print length, ',',dict,',',test

