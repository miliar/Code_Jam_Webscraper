class rc:
	def init(self):
		tmp = raw_input().split()
		self.R = int(tmp[0])
		self.k = int(tmp[1])
		self.n = int(tmp[2])
		self.visited = [False] * self.n
		self.guide = [None] * self.n
		tmp = raw_input().split()
		self.groups = [int(item) for item in tmp]

	def calcFromGroup(self, index):
		flag = index
		fee = 0
		while fee + self.groups[index] <= self.k:
			fee += self.groups[index]
			index += 1
			if (index >= self.n):
				index = 0
			if (index == flag):
				break
		self.guide[flag] = (fee, index)
	
	def calc(self):
		for idx in range(self.n):
			self.calcFromGroup(idx)
		pos = 0
		count = 0
		income = 0L
		while (count < self.R):
			income += self.guide[pos][0]
			self.visited[pos] = True
			pos = self.guide[pos][1]
			count += 1
			if (self.visited[pos] == True):
				break
		if (count == self.R):
			return income		
		circleIncome = 0
		circleCount = 0
		flag = pos
		while (count < self.R):
			circleIncome += self.guide[pos][0]
			pos = self.guide[pos][1]
			circleCount += 1
			if (pos == flag):
				break
		if (count == self.R):
			return income + circleIncome
		multiple = ((self.R - count) / circleCount)
		income += circleIncome * multiple
		count += circleCount * multiple
		while (count < self.R):
			income += self.guide[pos][0]
			pos = self.guide[pos][1]
			count += 1
		return income

def main():
	T = int(raw_input())
	case = 1
	while (case<=T):
		r = rc()
		r.init()
		print 'Case #%d: %d' % (case, r.calc())
		case += 1
	
if __name__ == '__main__':
	main()
