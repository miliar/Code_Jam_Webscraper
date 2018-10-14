import sys

class Input(object):
	def __init__(self):
		self._g = self._gen()

	def _gen(self):
		for line in sys.stdin:
			for token in line[:-1].split(' '):
				if token != '' or token:
					yield token

	def int(self):
		return int(self._g.next())

	def float(self):
		return float(self._g.next())

	def string(self):
		return self._g.next()

I = Input()

tc = I.int()
for cs in range(1,tc+1):
	c = I.float()
	f = I.float()
	x = I.float()
	k = x/c - 1 - 2/f
	if k < 0:
		k = 0
	else:
		k_i = round(k)
		if abs(k-k_i) <= 1e-9:
			k = int(k_i)
		else:	
			k = int(k) +1
	result = 0.0
	for i in range(k):
		result += c/(2 + i*f)
	result += x/(2+ k*f)
	print "Case #%d: %.10f" % (cs, result)
