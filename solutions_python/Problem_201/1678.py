from heapq import * 
import sys

sys.stdin = open('C-small-2-attempt0.in', 'r')
sys.stdout = open('C-small-2-sttempt0.out', 'w')

for t in range(int(input())):
	a, b = map(int, input().split())
	p, q = 0, 0

	h = [-a]

	for i in range(b):
		k = -heappop(h)
		p, q = k//2, (k-1)//2
		if p: heappush(h, -p)
		if q: heappush(h, -q)
	
	print('Case #%d:' % (t+1), p, q)
