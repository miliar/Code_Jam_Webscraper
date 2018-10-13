# Google CodeJam 2017
# Jan Hartman

class PancakeFlipper:
	def __init__(self, s, k, max_depth):
		self.k = k
		self.n = len(s)
		self.states = {}
		self.max = max_depth

	def search(self, s, count):
		if not ("-" in s):
			return count

		elif count > self.max:
			return -1

		if s in self.states and self.states[s] <= count:
			return -1

		self.states[s] = count

		new_best = -1
		for pos in range(self.n - self.k + 1):
			l = list(map(lambda x: x == "+", s))
			new_l = l[:pos] + list(map(lambda x: not x, l[pos:pos+self.k])) + l[pos+self.k:]
			new_s = "".join(map(lambda x: "+" if x else "-", new_l))
			new_c = self.search(new_s, count+1)

			if new_best < 0 or new_c < new_best and new_c > 0:
				new_best = new_c

		return new_best

t = int(input())
for case_no in range(t):
	s, k = input().split(" ")
	k = int(k)
	
	max_depth = 5
	count = -1

	while count == -1 and max_depth < 20:
		max_depth += 1
		pf = PancakeFlipper(s, k, max_depth)
		count = pf.search(s, 0)

	flips = "IMPOSSIBLE" if count < 0 else str(count)

	#print("states", pf.states)
	print("Case #{:d}: {:s}".format(case_no+1, flips))
