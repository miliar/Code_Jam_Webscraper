import sys

fi = iter(sys.stdin)
T = int(next(fi))

for t in xrange(T):
	N = int(next(fi))
	nao_blocks = sorted([float(tok) for tok in next(fi).split()])
	ken_blocks = sorted([float(tok) for tok in next(fi).split()])

	def deceit(nao, ken):
		pts = 0
		while nao:
			if nao[0] < ken[0]:
				nao = nao[1:]
				ken = ken[:-1]
			else:
				nao = nao[1:]
				ken = ken[1:]
				pts += 1
		return pts

	def real(nao, ken):
		pts = 0
		while nao:
			if nao[0] < ken[0]:
				nao = nao[1:]
				ken = ken[1:]
			else:
				nao = nao[:-1]
				ken = ken[1:]
				pts += 1
		return pts

	print 'Case #%d: %d %d' % (t + 1, deceit(nao_blocks, ken_blocks), real(nao_blocks, ken_blocks))
