import sys

lines = sys.stdin.readlines()
T = int(lines[0])
for t in range(T):
	N, K = (int(x) for x in lines[t+1].split())
	K += 1
	L = 1
	for i in range(N):
		L *= 2
	if K%L == 0:
		print ("Case #%d: ON" % (t+1,))
	else:
		print ("Case #%d: OFF" % (t+1,))
	
