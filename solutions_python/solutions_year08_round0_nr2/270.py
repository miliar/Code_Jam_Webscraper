import sys

N = int(sys.stdin.readline())

for i in range(N):
	turnaround = int(sys.stdin.readline())
	counts = sys.stdin.readline().split()
	acount = int(counts[0])
	bcount = int(counts[1])
	A = []
	B = []
	for j in range(acount):
		t = sys.stdin.readline().split()
		d = t[0].split(':')
		a = t[1].split(':')
		A.append((int(d[0]) * 60 + int(d[1]), int(a[0]) * 60 + int(a[1])))
	for j in range(bcount):
		t = sys.stdin.readline().split()
		d = t[0].split(':')
		a = t[1].split(':')
		B.append((int(d[0]) * 60 + int(d[1]), int(a[0]) * 60 + int(a[1])))
	A.sort()
	B.sort()
	trainsA = 0
	trainsB = 0
	atA = 1440
	atB = 1440
	while A or B:
		if atA < 1440:
			for t in range(len(A)):
				if atA <= A[t][0]:
					atB = A[t][1] + turnaround
					A.pop(t)
					break
			atA = 1440
		elif atB < 1440:
			for t in range(len(B)):
				if atB <= B[t][0]:
					atA = B[t][1] + turnaround
					B.pop(t)
					break
			atB = 1440
		elif not A:
			atB = B[0][0]
			trainsB = trainsB + 1
		elif not B:
			atA = A[0][0]
			trainsA = trainsA + 1
		elif B[0][0] < A[0][0]:
			atB = B[0][0]
			trainsB = trainsB + 1
		else:
			atA = A[0][0]
			trainsA = trainsA + 1
	print "Case #%d:" % (i + 1), trainsA, trainsB
