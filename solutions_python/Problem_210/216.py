CAMERON = 0
JAMIE = 1

# sort by start time
def sort_fun(p):
	return p[0]


def calc_min_exchanges(cact, jact):
	act = cact + jact

	act.sort(key=sort_fun)

	if len(act) <= 1:
		return 2

	tmax = [0, 0]
	cur_owner = act[0][2]
	swap = 0
	prev_time = act[0][0]

	# find min constraints by activities and count min/max time for each partner
	for a in act:
		if cur_owner != a[2]:
			swap += 1
			tmax[cur_owner] += a[0] - prev_time
			cur_owner = a[2]

		tmax[cur_owner] += a[1] - prev_time
		prev_time = a[1]

	day_end_time = (act[0][0] - act[-1][1]) % 1440
	tmax[cur_owner] += day_end_time
	if cur_owner != act[0][2]:
		tmax[act[0][2]] += day_end_time

	if tmax[0] >= 720 and tmax[1] >= 720:
		if swap % 2 == 0:
			return swap
		else:
			return swap + 1

	if tmax[0] < 720 and tmax[1] < 720:
		raise Exception("should not happen")

	if tmax[0] < 720:
		rich = 1
		tsum = tmax[0]
	else:
		rich = 0
		tsum = tmax[1]

	# if this is not enough, we need to add more double-swaps (+=2) going over the
	# deficient partner
	tlines = []

	for x in xrange(len(act)):
		# we need 2 consecutive "rich" partner activities
		if rich != act[x][2] or rich != act[(x - 1) % len(act)][2]:
			continue

		# add time between rich partner activities to our timelines
		tlines += [ (act[x][0] - act[x-1][1]) % 1440 ]

	tlines.sort(reverse=True)
	for t in tlines:
		swap += 2
		tsum += t
		if tsum >= 720:
			break

	if tsum < 720:
		raise Exception("should not happen2")

	if swap % 2 == 0:
		return swap
	else:
		return swap + 1

if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	t = int(lines[0])
	idx = 1
	for i in xrange(t):
		[cn, jn] = lines[idx].split(" ")
		cn = int(cn)
		jn = int(jn)
		idx += 1

		cact = []
		for x in xrange(cn):
			[start, end] = lines[idx + x].split(" ")
			cact += [(int(start), int(end), 0)]
		idx += cn

		jact = []
		for x in xrange(jn):
			[start, end] = lines[idx + x].split(" ")
			jact += [(int(start), int(end), 1)]
		idx += jn

		out.write("Case #%d: %d\n" % (i + 1, calc_min_exchanges(cact, jact)))

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
