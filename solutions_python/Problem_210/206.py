class Interval(object):
	def __init__(self, start, end, t=None):
		self.start = start
		self.end = end
		self.t = t
		self.length = end - start


def solve(intervals):
	if len(intervals) <= 1:
		return 2
	else:
		intervals.sort(key=lambda x: x.start)
		if intervals[1].t != intervals[0].t:
			return 2
		if intervals[1].end - intervals[0].start <= 720:
			return 2
		if intervals[0].end + 1440 - intervals[1].start <= 720:
			return 2
	return 4

t = int(raw_input())

for i in range(1, t + 1):
	C, J = map(int, raw_input().split())
	intervals = []
	for j in range(C):
		s1, s2 = map(int, raw_input().split())
		intervals.append(Interval(s1, s2, 'J'))
	for k in range(J):
		s1, s2 = map(int, raw_input().split())
		intervals.append(Interval(s1, s2, 'C'))
	print("Case #%d: %d" % (i, solve(intervals)))
