#!/usr/bin/env python
import sys,re

def read(filename):
	L=D=N=0
	words = []
	patterns = []
	for i,line in enumerate(file(filename)):
		if i==0: 
			L,D,N = map(int, line.split())
			continue
		if 1<=i<=D:
			words.append(line.strip())
			continue
		else:
			patterns.append(re.compile(line.strip().replace('(', '[').replace(')',']')))

	return L,D,N,words,patterns

def main(argv):
	L,D,N,words,patterns = read(argv[1])
	#print words
	#print patterns
	for i,p in enumerate(patterns):
		n=0
		for w in words:
			res = p.search(w)
			if(res): n+=1
		print "Case #%d: %d" % (i+1,n)

if __name__ == "__main__":
	main(sys.argv)
