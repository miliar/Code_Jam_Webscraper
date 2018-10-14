#!/usr/bin/python
T=int(raw_input())

for case in range(T):
	r=raw_input().split()
	n=int(r[0])
	k=int(r[1])
	k=k%(2**n)
	if k==(2**n-1):
		print "Case #"+str(case+1)+": ON"
	else:
		print "Case #"+str(case+1)+": OFF"
