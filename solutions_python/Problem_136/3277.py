import sys

class Input(object):
	def __init__(self, c, f, x):
		# cookie farm cost
		self.cost = c
		# cookies per second per farm
		self.farmIncome = f
		# win with this many cookies
		self.goal = x
		self.baseIncome = 2

	def run(self):
		elapsed = 0.0
		num_farms = 0
		prev_seconds = elapsed + self.secondsToWin(num_farms)
		cur_seconds = prev_seconds
		#print self
		#print "%d farms, %f elapsed, total %f" % (num_farms, elapsed, cur_seconds)
		while cur_seconds <= prev_seconds:
			prev_seconds = cur_seconds
			elapsed += self.secondsToNextFarm(num_farms)
			num_farms += 1
			cur_seconds = elapsed + self.secondsToWin(num_farms)
			#print "%d farms, %f elapsed, total %f" % (num_farms, elapsed, cur_seconds)
		return prev_seconds

	def income(self, num_farms):
		return self.baseIncome + self.farmIncome * num_farms

	def secondsToNextFarm(self, num_farms):
		return self.cost / self.income(num_farms)

	def secondsToWin(self, num_farms):
		return self.goal / self.income(num_farms)
	
	def __str__(self):
		return str((self.cost, self.farmIncome, self.goal))

def parse(line):
	c, f, x = line.split()
	return Input(float(c), float(f), float(x))

def main():
	lines = [line for line in sys.stdin]
	# first line is number of test cases == number of other lines
	num_test_cases = int(lines[0])
	lines = lines[1:]
	assert num_test_cases == len(lines)
	for i, line in enumerate(lines):
		result = parse(line).run()
		print "case #%d: %f" % (i+1, result)

main()
