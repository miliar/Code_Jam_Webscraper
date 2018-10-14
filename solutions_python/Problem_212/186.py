from __future__ import print_function
import sys
from sys import stdin

from collections import Counter

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ln(f=int):
	return list(map(f,stdin.readline().strip().split()))

T, = ln()
INF = float('inf')

for test in range(T):
	N,P = ln()
	G = ln()

	G = [g % P for g in G]
	h = Counter(G)



	if P == 2:
		res = h[0] + ((h[1]+1)//2)
	elif P == 3:
		if h[1] >= h[2]:
			res = h[0] + h[2]
			h[1] -= h[2]
			res += (h[1]//3) + (0 if (h[1]%3==0) else 1)
		else:
			res = h[0] + h[1]
			h[2] -= h[1]
			res += (h[2]//3) + (0 if (h[2]%3==0) else 1)
	elif P ==4:
		res = h[0]
		h[0] = 0

		res += h[2]//2
		h[2] = h[2]%2

		if h[1] >= h[3]:
			res += h[3]
			h[1] -= h[3]
			h[3] = 0
		else:
			res += h[1]
			h[3] -= h[1]
			h[1] = 0



		if h[2] == 1:
			res += 1
			h[2] -= 1
			if h[1] != 0:
				h[1] -= 2
				h[1] = max(0,h[1])
			elif h[3] != 0:
				h[3] -= 2
				h[3] = max(0,h[3])


		if h[1] != 0:
			res += (h[1]//4) + (0 if (h[1]%4==0) else 1)
		elif h[3] != 0:
			res += (h[3]//4) + (0 if (h[3]%4==0) else 1)
	




	print ("Case #" + str(test+1) + ": " + str(res))
	



