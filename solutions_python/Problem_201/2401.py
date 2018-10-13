import sys
import re

file = open(sys.argv[1])
T = None
Case = 1

for row in file:
	if T is None:
		T = int(row)
		continue
	N = int(row.split(' ')[0])
	K = int(row.split(' ')[1])

	#if K > int(N / 2.0 + 0.5) or N == K:
	if N == K:
		S_R = 0
		S_L = 0
	else:
		bathroom = [str(i) for i in range(0, N)]
		start = 0
		end = N - 1
		for i__ in range(0, K):
			S = int((end - start) / 2) + start
			S_R = end - S
			S_L = S - start
			bathroom[S] = '-'
			next = ','.join(bathroom).split('-')
			rooms = [len([i for i in i.split(',') if i !=''  ]) for i in next]
			next = [i for i in next[rooms.index(max(rooms))].split(',') if i != '']
			start = int(next[0])
			end = int(next[-1])

	print("Case #%d: %d %d" % (Case, max(S_R, S_L), min(S_R, S_L)))
	Case = Case + 1
	T = T - 1
	if T == 0:
		break
