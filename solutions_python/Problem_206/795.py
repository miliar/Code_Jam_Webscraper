class Horse:
	def __init__(self, k, s):
		self.position = k
		self.speed = s

def solve():
	D, N = map(int, raw_input().strip().split())
	horses = []
	for i in xrange(N):
		K, S = map(int, raw_input().strip().split())
		horse = Horse(K, S)
		horses += [horse]
	maxval = 0.0
	for i in sorted(horses, key=lambda x:x.position, reverse=True):
		val = (D-i.position)/float(i.speed)
		if val > maxval:
			maxval = val
	return "%.6f"%(D/maxval)

if __name__ == "__main__":
	for i in xrange(input()):
		print "Case #"+str(i+1)+": "+str(solve())
