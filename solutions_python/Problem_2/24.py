#!/usr/bin/env python

INPUT_FILE = 'B-large.in'

def process(case, turnaround, sched_ab, sched_ba):
	sched_ab.sort(cmp = lambda a, b: cmp(a[0], b[0]))
	sched_ba.sort(cmp = lambda a, b: cmp(a[0], b[0]))

	new_ab = 0
	new_ba = 0

	has_ab = 0
	has_ba = 0

	turned_ab = [0] * (24 * 60 + 60)
	turned_ba = [0] * (24 * 60 + 60)

	current = 0
	while current < 24 * 60:
		has_ab = has_ab + turned_ab[current]
		has_ba = has_ba + turned_ba[current]

		while len(sched_ab) > 0 and sched_ab[0][0] == current:
			if has_ab > 0:
				has_ab = has_ab - 1
				#print current, "reusing a->b"
			else:
				new_ab = new_ab + 1
				#print current, "new a->b"
			turned_ba[sched_ab[0][1] + turnaround] = turned_ba[sched_ab[0][1] + turnaround] + 1
			sched_ab.pop(0)

		while len(sched_ba) > 0 and sched_ba[0][0] == current:
			if has_ba > 0:
				has_ba = has_ba - 1
				#print current, "reusing b->a"
			else:
				new_ba = new_ba + 1
				#print current, "new b->a"
			turned_ab[sched_ba[0][1] + turnaround] = turned_ab[sched_ba[0][1] + turnaround] + 1
			sched_ba.pop(0)

		current = current + 1

	print 'Case #%d: %d %d' % (case, new_ab, new_ba)

def read_timetable(sched, count, fp):

	def time_to_int(time):
		hour, min = map(int, time.split(':'))
		return hour * 60 + min

	for i in range(count):
		depature, arrival = fp.readline().split()
		pair = (time_to_int(depature), time_to_int(arrival))
		assert(pair[0] != pair[1])
		sched.append(pair)

fp = open(INPUT_FILE, 'r')

n = int(fp.readline())

for case in range(1, n + 1):
	sched_ab = []
	sched_ba = []

	turnaround = int(fp.readline())
	count_ab, count_ba = map(int, fp.readline().split())
	read_timetable(sched_ab, count_ab, fp)
	read_timetable(sched_ba, count_ba, fp)
	process(case, turnaround, sched_ab, sched_ba)

fp.close()
