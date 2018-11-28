T = int(raw_input())

for case in range(1, T+1):
	N = int(raw_input())
	A = []
	B = []
	intersections = 0
	
	for i in range(N):
		nextA, nextB = map(int, raw_input().split())
		for j in range(len(A)):
			if (nextA - A[j]) * (nextB - B[j]) < 0:
				intersections += 1
		A.append(nextA)
		B.append(nextB)

	print 'Case #' + str(case) + ': ' + str(intersections)

