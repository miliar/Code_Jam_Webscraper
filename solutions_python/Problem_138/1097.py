import sys
from collections import deque
sys.stdin = open ('D-large.in')
sys.stdout = open ('D.txt','w')
T = int(input().strip())
for z in range (T):
	N = int(input().strip())
	n = sorted(list(map(float,input().strip().split())))
	k = sorted(list(map(float,input().strip().split())))
	d,o = 0,0
	nd = deque(n[:])
	kd = deque(k[:])
	for i in range (N):
		if nd[0]>kd[0]:
			d+=1
			nd.popleft()
			kd.popleft()
		else:
			nd.popleft()
			kd.pop()
	no = deque(n[:])
	ko = deque(k[:])
	for i in range (N):
		if len(ko)<1: break
		if no[0]>ko[0]:
			cur = 0
			while True:
				if cur == len(ko) or no[0]<ko[cur]:
					no.popleft()
					ko = deque(list(ko)[cur+1:])
					break	
				else:
					o+=1
					cur+=1
		else:
			no.popleft()
			ko.popleft()
	print ('Case #{0}:'.format(z+1),str(d),str(o))
sys.stdout.close()