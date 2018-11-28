#!/usr/bin/env python
def times(positions):
	times=[]
	if not positions:return times
	times.append(positions[0])
	for p in range(1, len(positions)):
		times.append(abs(positions[p]-positions[p-1])+1+times[-1])
	return times

from sys import stdin
T=int(stdin.readline())
for case in range(1, T+1):
	Order=stdin.readline().split()
	N=int(Order.pop(0))
	order=map(lambda x:x=='O', Order[0::2])
	position=map(int, Order[1::2])
	positions=[[], []]
	for n in range(N):
		positions[order[n]].append(position[n])
	time=map(times, positions)
	I=[0, 0]
	W=[0, 0]
	T=time[order[0]][0]
	I[order[0]]=1
	for n in range(1, N):
		r=order[n]
		t=time[r]
		if t[I[r]]+W[r]<=T:
			W[r]+=T+1-t[I[r]]-W[r]
		T=t[I[r]]+W[r]
		I[r]+=1
	print "Case #%d: %d"%(case, T)
