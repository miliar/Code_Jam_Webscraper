#!/usr/bin/python 
from sys import argv
import re
from math import pow,floor,log10

input = [ "ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"]
output = ["our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"]
mappings = {'z':'q','q':'z'} 
for x,v in zip(input,output):
	for i,j in zip(x,v):
		mappings[i] = j 
for x in 'abcdefghijklmnopqrstuvwxyz':
	if x not in mappings:
		mappings[x] = x

with open(argv[1],'r') as f:
	numCases = int(f.readline())
	casenum = 1
	while(casenum <= numCases):
		line = f.readline().strip()
		print 'Case #%d: %s' %(casenum,''.join(map(lambda x: mappings[x],line)))
		casenum +=1
