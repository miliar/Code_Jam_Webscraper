class Dancers(object):
	def setup(self, surpise, p, scores):
		self._surprise_allowed = surpise
		self._pval = p
		self._regular_min_score = p*3 - 2
		self._surprise_min_score = p*3 - 4
		self._dancer_points = [score for score in scores]
		self._p_reachable = 0
	def calc_p_reachable(self):
		already_surprised = 0
		for score in self._dancer_points:
			if self._pval == 0:
				self._p_reachable += 1
				continue
			if score == 0:	# self._pval will not be 0 here
				continue
			if score >= self._regular_min_score:
				self._p_reachable += 1
				continue
			if (score >= self._surprise_min_score and 
				already_surprised < self._surprise_allowed):
				already_surprised += 1
				self._p_reachable += 1
				continue
		return self._p_reachable

if __name__ == '__main__':
	tests = int(raw_input())
	casei = 0
	while tests > 0:
		tests -= 1
		casei += 1
		d = Dancers()
		testdata = raw_input().split()
		s = int(testdata[1])
		p = int(testdata[2])
		N = int(testdata[0])
		sc = []
		for idx in range(N):
			sc.append(int(testdata[3+idx]))
		d.setup(s, p, sc)
		print "Case #%d: %d"%(casei, d.calc_p_reachable())
