from math import floor, sqrt

def solve(r,t):
	delta = 4*r*r-4*r+1+8*t
	ans = int(floor((1-2*r+sqrt(float(delta)))/4))
	if 2*ans*ans + (2*r-1)*ans - t <= 0:
		return ans
	else:
		return ans-1
	
T = int(raw_input())

for i in range(T):
	r, t = map(int, raw_input().strip().split())
	print 'Case #%d: %d' %(i+1, max(solve(r,t),0)),
	if i < T-1: print
	