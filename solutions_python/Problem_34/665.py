#!/usr/bin/python 
import sys
import re
import copy

infile=open(sys.argv[1]) 
outfile=open(sys.argv[1].split(".")[0]+".out","w")
(L,D,N)=tuple([int(i) for i in infile.readline().split()])
pat_re=re.compile("(\([a-z]*\)|[a-z])"*L)

alien_dict=[]
for i in range(0,D):
	word=infile.readline().strip()
	alien_dict.append(word)
for i in range(0,N):
	dict_copy=copy.copy(alien_dict)
	pat=infile.readline().strip()
	m=pat_re.match(pat)
	#print pat
	for l in range(0,L):
		g=m.group(l+1)
		s=(set([g]) if len(g)==1 else set(c for c in g[1:-1]) )
		#print dict_copy,"*",s,"=",
		dict_copy=filter(lambda x:x[l] in s,dict_copy)
		#print dict_copy
	outfile.write("Case #%d: %d\n"%(i+1,len(dict_copy)))
	
	
