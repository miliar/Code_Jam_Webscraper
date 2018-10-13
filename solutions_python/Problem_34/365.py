import re

L,D,N=map(int, re.match("(\d+)\s*(\d+)\s*(\d+)",raw_input().strip()).groups())
words=' '.join([raw_input().strip() for i in range(D)])

for i in range(N):
	s=raw_input().strip().replace('(','[').replace(')',']')
	r=re.findall("%s" % s, words)
	print "Case #%d: %d" % (i+1, len(r))
	

