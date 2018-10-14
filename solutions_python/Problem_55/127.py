#! /usr/bin/python

from sys import stdin

def simulate(sizes,rides,k):
	r=rides
	money=[]
	seen={}
	cur=0
	step=0
	while cur not in seen and r>0:
		left=k
		seen[cur]=step
		step+=1
		r-=1
		old_cur=cur
		mon=0
		groups_left=len(sizes)
		while left>=sizes[cur] and groups_left>0:
			mon+=sizes[cur]
			left-=sizes[cur]
			cur=(cur+1)%len(sizes)
			groups_left-=1
		money.append(mon)
		
	total_money=sum(money)
	if r==0:
		return total_money
	cycle_start=seen[cur]
	cycle_money=sum(money[cycle_start:])
	startup=total_money-cycle_money
	cycle_len=len(money[cycle_start:])
	rides-=cycle_start
	cycles=rides/cycle_len
	extras=rides%cycle_len
	return startup+cycle_money*cycles+sum(money[cycle_start:cycle_start+extras])

if __name__=='__main__':
	T=int(stdin.readline())
	for case in xrange(1,T+1):
		R,k,N=map(int,stdin.readline().split())
		sizes=map(int, stdin.readline().split())
		print "Case #%d: %d"%(case, simulate(sizes,R,k))
