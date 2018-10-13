#!/usr/bin/python
import sys

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

tc=int(f.readline())
for i in range(1,tc+1):
	ln = f.readline().split()
	bs = int(ln[0])
	n = int(ln[1])

	spaces={bs:1}
	while n>0:
		sel=max(spaces.keys())
		cnt=spaces.pop(sel)
		lft=(sel-1)//2
		rht=(sel-1)-lft
		spaces[lft]=cnt+spaces.get(lft,0)
		spaces[rht]=cnt+spaces.get(rht,0)
		n -= cnt
		
	print("Case #{}: {} {}".format(i,rht,lft))

