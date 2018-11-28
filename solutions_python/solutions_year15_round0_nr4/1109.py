import sys
from heapq import heappush,heappop

def brute(X,R,C): # 4<=X<=6, max(R,C)>X, (R*C)%X==0
	if(X==4 and min(R,C) == 2): return True
	if(X==5 and min(R,C) == 3): return True
	return False

def solve(X,R,C): # Is there a very ulgy X-ominoe?
	if(X>max(R,C) or X>=7): return True # | or o
	if((R*C)%X != 0): return True
	if((X+1)//2 > min(R,C)): return True # L
	if(X<=3): return False
	return brute(X,R,C)

def main():
	sys.stdout = open('small2.out','w')
	stdin  = open('small2.in','r')
	#stdin  = open('test.in','r')
	casos = int(stdin.readline())
	for caso in range(casos):
		(X,R,C) = (int(s) for s in stdin.readline().strip().split(' '))
		ans = solve(X,R,C)
		print('Case #{0}: {1}'.format(caso+1,'RICHARD' if(ans) else 'GABRIEL'))

main()
