if __name__ == '__main__':
	INF = open('in', 'r')
	OUTF = open('out', 'w')
	N = int(INF.readline())

	for case in range(N):
		B = int(INF.readline())
		naomi = map(float, sorted(INF.readline().rstrip('\n').split(' ')))
		ken = map(float, sorted(INF.readline().rstrip('\n').split(' ')))
		dsn = 0
		wsn = 0

		naomix = list(naomi)
		kenx = list(ken)
		for i in range(B):
			if kenx[-1] > naomix[-1]:
				del naomix[0]
				del kenx[-1]
			else:
				del naomix[-1]
				del kenx[-1]
				dsn += 1

		naomix = list(naomi)
		kenx = list(ken)
		for i in range(B):
			g = filter(lambda x: x > naomix[-1], kenx)
			if len(g) > 0:
				del naomix[-1]
				kenx.remove(g[0])
			else:
				del naomix[-1]
				del kenx[0]
				wsn += 1

		OUTF.write('Case #' + str(case + 1) + ': ' + str(dsn) + ' ' + str(wsn) + '\n')
