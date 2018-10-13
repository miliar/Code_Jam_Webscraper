if __name__ == '__main__':
	INF = open('in', 'r')
	OUTF = open('out', 'w')
	N = int(INF.readline())

	for t in range(N):
		g1 = []
		g2 = []

		a1 = int(INF.readline())
		for i in range(4):
			r = INF.readline().rstrip('\n').split(' ')
			g1.append(r)

		a2 = int(INF.readline())
		for i in range(4):
			r = INF.readline().rstrip('\n').split(' ')
			g2.append(r)

		ansl = []
		ansl.append(g1[a1 - 1])
		ansl.append(g2[a2 - 1])

		seen = set()
		repeated = set()
		for l in ansl:
			for i in set(l):
				if i in seen:
					repeated.add(i)
				else:
					seen.add(i)

		ans = ''
		leng = len(repeated)
		if leng < 1:
			ans = 'Volunteer cheated!'
		elif leng == 1:
			ans = str(repeated.pop())
		else:
			ans = 'Bad magician!'

		OUTF.write('Case #' + str(t + 1) + ': ' + ans + '\n')
