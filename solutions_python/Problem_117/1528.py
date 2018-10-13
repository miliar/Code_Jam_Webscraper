#!/usr/bin/python

T = int(raw_input().strip())
for i in range(1, T+1):
	N, M = raw_input().strip().split(" ")
	N = int(N)
	M = int(M)
	A = [raw_input().strip().split(" ") for j in range(0,N) ]
	rows = [0 for j in range(0, N)]
	cols = [0 for j in range(0, M)]
	R = [[0 for k in range(0, M)] for j in range(0, N)]
	L = []
	for row in A:
		L.extend(row)
	L = list(set(L))
	L.sort(reverse = True)
	for e in L:
		for x in range(0, N):
			if(A[x].count(e) > 0):
				for y in range(0, M):
					if(A[x][y] == e):
						if(rows[x] == 0):
							rows[x] = 1
							for index in range(0, M):
								R[x][index] = e						
						if(cols[y] == 0):
							cols[y] = 1
							for index in range(0, N):
								R[index][y] = e
					
	if(R == A):
		print "Case #" + str(i) + ": YES"
	else:
		print "Case #" + str(i) + ": NO"
