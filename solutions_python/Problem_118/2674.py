import sys
import math

class input(object):
	def __init__(self):
		lines = sys.stdin.readlines()
		cases = int(lines[0].strip())
		for l in range(1, cases + 1):
			line = lines[l].strip().split(' ')
			low = int(line[0])
			high = int(line[1])
			o = sqpalin(low, high)
			c = o.run()
			print('Case #%d: %d' % (l, c))

class sqpalin(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high

	def run(self): # get number of squared palinfromes
		pocet = 0
		for n in range(self.low, self.high + 1):
			z = str(n)
			r = z[::-1]
			if z == r:
				sr = int(math.sqrt(n))
				if sr * sr == n:
					s = str(sr)
					sr = s[::-1]
					if s == sr:
						pocet = pocet + 1
		return pocet
				
i = input()


