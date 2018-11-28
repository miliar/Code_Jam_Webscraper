from __future__ import division

def problem(cost, rate, goal):
	n = 0
	t = 0
	r = 2
	timetogoal = float('inf')
	while n < goal:
		new_timetogoal = t+goal/r
		if new_timetogoal > timetogoal: break
		else: timetogoal = new_timetogoal
		# print timetogoal

		timetobuy = cost/r
		t += timetobuy
		r += rate

	return timetogoal

def main():
	casenums = int(stdin.readline())
	for casenum in xrange(1,casenums+1):
		C, F, X = map(float, stdin.readline().split(' '))
		msg = problem(C, F, X)
		print 'Case #%d: %s' % (casenum, msg)

if __name__ == '__main__':
	from sys import stdin
	main()
