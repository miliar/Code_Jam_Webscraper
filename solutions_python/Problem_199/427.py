#!/usr/bin/python
import sys

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

tc=int(f.readline())
for i in range(1,tc+1):
	ln=f.readline().split()
	ck=ln[0]
	sz=int(ln[1])

	cnt=0
	rep=1

	while rep:
		cs=len(ck)
		j=ck.find("-")
		if j==-1:
			rep=0
		elif j+sz>cs:
			rep=0
			cnt=-1
		elif j+sz==cs:
			rep=0
			if ck[j:]=='-'*sz:
				cnt+=1
			else:
				cnt=-1
		else:
			cnt+=1
			ck=ck[j:j+sz].replace('+','.').replace('-','+').replace('.','-')+ck[j+sz:]
					
					
	print("Case #{}: {}".format(i,"IMPOSSIBLE" if cnt<0 else cnt))

