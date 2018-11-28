inf = open('a-large.in', 'r')
outf = open('wireAns.txt', 'w')

T = int(inf.readline())
for i in xrange(T):
	relation = {}
	A = []
	B = []
	ans = 0
	counting = [1 for j in xrange(10001)]
	c = inf.readline()
	for j in xrange(int(c)):
		d = inf.readline()
		d = map(int, d.split())
		relation[d[0]] = d[1]
		A.append(d[0])
		B.append(d[1])
	A.sort()
	B.sort()
	for k in A:
		Bx = relation[k]
		for m in xrange(len(B)):
			if B[m] == Bx:
				counting[m] = 0
				break
			else:
				ans += counting[m]
	outf.write('Case #' + str(i+1) + ': ' + str(ans) + '\n')

inf.close()
outf.close()
		