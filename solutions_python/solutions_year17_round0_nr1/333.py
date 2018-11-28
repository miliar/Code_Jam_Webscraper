import sys

IN = open('in.txt', 'r+')
sys.stdout = open('out.txt', 'w+')

TC = int(IN.readline())
for _ in xrange(TC):
	s, k = IN.readline().split()

	k = int(k)
	res = 0

	A = [0] * len(s)
	for i in xrange(len(s)):
		if s[i] == '+':
			A[i] = 1

	for i in xrange(len(s)-k+1):
		if A[i] == 0:
			for j in xrange(i, i+k):
				if A[j] == 1:
					A[j] = 0
				elif A[j] == 0:
					A[j] = 1

			res += 1

	if A.count(1) == len(s):
		print("Case #{0}: {1}".format(_+1, res))
	else:
		print("Case #{0}: IMPOSSIBLE".format(_+1))