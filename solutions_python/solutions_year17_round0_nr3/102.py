# -*- coding:utf-8 -*-

def cool() :
	0

T = int(input())

for c_n in range(1, T+1):
	(N, K) = input().split()
	N = int(N)
	K = int(K)
	lst = [0] * (N+1)
	lst[N] = 1
	look = N
	L = 0
	R = 0
	for i in range(0, K):
		while lst[look] == 0:
			look -= 1
		lst[look] -= 1
		L = (look - 1) // 2
		R = look - 1 - L
		lst[L] += 1
		lst[R] += 1
		
	print ("Case #{}: {} {}".format(c_n, R, L))