
class Robot(object):
	def __init__(self):
		self.pos = 1
		self.timer = 0

	def distance(self, pos):
		return abs(self.pos - pos)

	def move_to(self, pos, time):
		d = self.distance(pos)
		self.timer = max(min(self.timer, time) + d, time) + 1
		self.pos = pos
		return self.timer

def solve(data):
	now = 0
	robots = {'B': Robot(), 'O': Robot()}

	for name, pos in data:
		now = robots[name].move_to(pos, now)

	return now

def get_input():
	s = raw_input().split()
	N = int(s[0])
	RPs = [(s[i * 2 + 1], int(s[i * 2 + 2])) for i in xrange(N)]
	return RPs

def main():
	T = int(raw_input())
	for i in xrange(T):
		print 'Case #%d: %d' % (i + 1, solve(get_input()))

if __name__ == '__main__':
	main()
