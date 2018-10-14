#!/usr/bin/python
import sys

fi = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
fo = open(".".join(sys.argv[1].split('.')[:-1])+".out","w") if len(sys.argv) > 1 else sys.stdout

TC=int(fi.readline())
for i in range(1,TC+1):
	ln=fi.readline().split()
	D=int(ln[0])
	N=int(ln[1])
	Tmax=0
	for n in range(N):
		ln=fi.readline().split()
		K=int(ln[0])
		S=int(ln[1])
		tm=(D-K)/S
		if (Tmax<tm):
			Tmax=tm
	
					
	print("Case #{}: {}".format(i,D/Tmax),file=fo)

