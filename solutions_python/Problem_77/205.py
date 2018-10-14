import copy
for casenum in xrange(1,1+int(raw_input())):
	n = int(raw_input())
	N = [int(z) for z in raw_input().split()]
	B = copy.copy(N)
	B.sort()
	sum = 0
	for i in xrange(0,n):
		if B[i] != N[i]:
			sum += 1
	print 'Case #{0:d}: {1:.6f}'.format(casenum,sum)		