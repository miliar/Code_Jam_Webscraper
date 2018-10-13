import sys

T = raw_input()
for i in range(int(T)):
	s = raw_input()
	N = int(s.split()[0])
	S = int(s.split()[1])
	p = int(s.split()[2])

	ti = []
	for j in range(N):
		ti.append(int(s.split()[3 + j]))

	count = 0
	sur = 0
	ti.sort(reverse=True)
	for j in range(len(ti)):
		if p > ti[j]:
			continue

		if p * 3 - 2 <= ti[j]:
			count = count + 1
		elif p * 3 - 4 <= ti[j] and sur < S:
			count = count + 1
			sur = sur + 1

	sys.stdout.write("Case #%d: %d\n" % (i + 1, count))
