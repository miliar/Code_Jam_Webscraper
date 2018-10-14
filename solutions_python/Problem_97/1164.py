
class CountRecycle(object):
	def setup(self, a, b):
		self._aL = self.get_list(a)
		self._bL = self.get_list(b)
		self._a = a
		self._b = b
		self._diglen = len(self._aL)
	def get_number(self, char_list):
		st = ''.join(char_list)
		return int(st)
	def get_rotation(self, origin_list, start):
		return origin_list[start:] + origin_list[:start]
	def get_list(self, number):
		st = str(number)
		return list(st)
	def fromAtoB(self):
		return [num for num in range(self._a, self._b+1)]
	def MainCount(self):
		longlist = self.fromAtoB()
		matchCount = 0
		for num in longlist:
			nl = self.get_list(num)
			checkl = []
			for splitpoint in range(1, self._diglen):
				newl = self.get_rotation(nl, splitpoint)
				new_num = self.get_number(newl)
				if new_num > num and new_num <= self._b:
					if new_num not in checkl:
						checkl.append(new_num)
						matchCount += 1
		return matchCount

if __name__ == '__main__':
	c = CountRecycle()
	total = int(raw_input())
	case = 0
	while total > 0:
		total -= 1
		case += 1
		A,B = raw_input().split()
		c.setup(int(A), int(B))
		print "Case #%d: %d"%(case, c.MainCount())
