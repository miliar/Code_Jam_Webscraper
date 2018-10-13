if __name__ == '__main__':
	INF = open('in', 'r')
	OUTF = open('out', 'w')
	N = int(INF.readline())
	R = 2.0

	for case in range(N):
		v = INF.readline().rstrip('\n').split(' ')
		C = float(v[0])
		F = float(v[1])
		X = float(v[2])
		
		r = R
		s = X/r
		nof = X/C
		tfs = 0

		for i in range(int(nof)):
			fs = C/r
			tfs += fs
			r += F
			xs = X/r
			if tfs + xs >= s: break
			s = tfs + xs

		OUTF.write('Case #' + str(case + 1) + ': ' + str(s) + '\n')
