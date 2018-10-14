#!/usr/bin/python3

t = int(input())
for i in range(t):
	n = int(input())
	mns = sorted(map(float, input().split()))
	mks = sorted(map(float, input().split()))

	npw = 0
	mnsw = [m for m in mns] 
	mksw = [m for m in mks]
	for j in range(n):
		if mnsw[-1] > mksw[-1]:
			npw += 1
			mnsw.pop()
			mksw.pop(0)
		else:
			for k in range(n-j):
				if mksw[k] > mnsw[-1]:
					mksw.pop(k)
					break
			mnsw.pop()

	npdw = 0
	mnsw = [m for m in mns] 
	mksw = [m for m in mks]
	for j in range(n):
		if mnsw[0] > mksw[0]:
			npdw += 1
			mnsw.pop(0)
			mksw.pop(0)
		else:
			mnsw.pop(0)
			mksw.pop()

	print('Case #%d: %d %d' % (i+1, npdw, npw))
	
