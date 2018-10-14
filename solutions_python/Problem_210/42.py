from collections import namedtuple

HALF_A_DAY = 720

Interval = namedtuple('Interval', ['start', 'end', 'type'])



def main():
	num_tests = int(input())

	for t in range(num_tests):
		solve(t+1)

def solve(case):
	num_cameron_acts, num_jamie_acts = [int(x) for x in input().split(' ')]

	intervals = []

	for i in range(num_cameron_acts):
		start, end = [int(x) for x in input().split(' ')]
		intervals.append(Interval(start, end, 'cameron'))

	for i in range(num_jamie_acts):
		start, end = [int(x) for x in input().split(' ')]
		intervals.append(Interval(start, end, 'jamie'))

	intervals.sort()

	new_intervals = []

	for i in range(len(intervals)):
		j = (i+1)%len(intervals)
		start = intervals[i].end
		end = intervals[j].start
		new_type = get_interval_type(intervals[i].type, intervals[j].type)
		new_intervals.append(Interval(start, end, new_type))

	intervals.extend(new_intervals)

	cameron_join_time = sum(length(interval) for interval in intervals if 'cameron' in interval.type)
	jamie_join_time = sum(length(interval) for interval in intervals if 'jamie' in interval.type)

	overtime = None
	overtype = None

	if cameron_join_time > HALF_A_DAY:
		overtime = cameron_join_time
		overtype = 'ideally_cameron'
	elif jamie_join_time > HALF_A_DAY:
		overtime = jamie_join_time
		overtype = 'ideally_jamie'

	num_changes = 0

	if overtime is not None:
		diff = overtime - HALF_A_DAY
		good_edges = [length(interval) for interval in intervals if interval.type == overtype]
		good_edges.sort(reverse=True)
		val = 0
		used = 0 
		while val < diff:
			val += good_edges[used]
			used += 1

		num_changes += 2*used

	num_changes += sum(1 for interval in intervals if interval.type == 'neutral')

	print('Case #{}: {}'.format(case, num_changes))


def get_interval_type(type1, type2):
	if type1 != type2:
		return 'neutral'
	elif type1 == 'cameron':
		return 'ideally_cameron'
	elif type2 == 'jamie':
		return 'ideally_jamie'

def length(interval):
	start, end, _ = interval
	diff = end - start
	if diff < 0:
		diff += 2*HALF_A_DAY
	return diff

main()