def parse_time(s):
	h, m = map(int, s.split(':'))
	return m + h * 60

def main():
	n = int(raw_input())
	for num in range(n):

		t = int(raw_input())

		na, nb = map(int, raw_input().split(' '))

		events = []	# Time, -dTrains, station

		for x in range(na):
			departs, arrives = map(parse_time, raw_input().split(' '))
			events.append((departs, 1, 0))
			events.append((arrives + t, -1, 1))

		for x in range(nb):
			departs, arrives = map(parse_time, raw_input().split(' '))
			events.append((departs, 1, 1))
			events.append((arrives + t, -1, 0))

		events.sort()

		initial_trains = [0, 0]
		trains_ready = initial_trains[:]

		for time, dt, station in events:
			#print time, station, -dt
			new_ready = trains_ready[station] - dt
			if new_ready == -1:
				# Oops. Pretend we started with one more...
				initial_trains[station] += 1
				new_ready = 0
			trains_ready[station] = new_ready

		print "Case #%d: %d %d" % (num + 1, initial_trains[0], initial_trains[1])

main()
