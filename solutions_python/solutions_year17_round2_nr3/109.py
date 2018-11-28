import sys


te = input()

for qe in range(1, te+1):
	print >> sys.stderr, str(qe)+'/'+str(te)+' started ...'

	n, q = map(int, raw_input().split())

	e = [0]*n
	s = [0]*n

	for i in range(n):
		e[i], s[i] = map(int, raw_input().split())

	d = [[[0]*n] for _ in range(n)]

	for i in range(n):
		d[i] = map(int, raw_input().split())

	anss = []
	for _ in range(q):
		u, v = map(int, raw_input().split())

		# small dataset
		t = [9999999999999999]*n
		t[n-1] = 0

		for i in range(n-2, -1, -1):

			dist = 0
			for j in range(i+1, n):
				dist += d[j-1][j]

				if e[i] < dist:
					break

				if dist*1.0/s[i] + t[j] < t[i]:
					t[i] = dist*1.0/s[i] + t[j]



		anss.append(t[0])

	print 'Case #{}: {}'.format(qe, ' '.join('{:.7f}'.format(i) for i in anss))