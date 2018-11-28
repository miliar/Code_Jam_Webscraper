from random import uniform, random
from string import split, strip
import sys


def read_input(fname):
	cases = []
	infile = open(fname, 'rt')
	
	N = int(infile.readline())	
	for i in range(N):
		T = int(infile.readline())
		(NA, NB) = map(int, split(infile.readline()))
		
		trips_from_a = []
		for a in range(NA):
			trips_from_a.append(tuple(split(infile.readline())))
	
		trips_from_b = []
		for b in range(NB):
			trips_from_b.append(tuple(split(infile.readline())))

		cases.append((T, trips_from_a, trips_from_b))
 	return cases


def cmp_keys(p1, p2):
	"""
	In order to sort a list, we need a compare function for elements of the list.
	function compares two sequences based on a standard compare of their first
	element. So, you can use this to sort a list of (key, val) pairs by key.
	"""
	# note!!! Need to process arrivals before departures, if they're at the
	# same station and time
	(t1, e1) = p1
	(t2, e2) = p2
	
	if t1 != t2:
		return cmp(t1, t2)
	else:
		a1 = e1[1]
		a2 = e2[1]
		return -cmp(a1, a2) # arrival is +1, departure is -1
	
	
def to_minutes(hh_mm_str):
	"""
	Convert a time in hh:mm format to minutes
	"""
	(h, m) = map(int, split(hh_mm_str, ':'))
	assert(h >= 0 and h < 24)
	assert(m >= 0 and m < 60)
	return int(60 * h + m)


def build_event(da, depart_station, arrive_station, turn_around_minutes):
	t_depart = to_minutes(da[0])
	t_ready = to_minutes(da[1]) + turn_around_minutes
	return ((t_depart, (depart_station, -1)), (t_ready, (arrive_station, +1)))

			
def main():
 	inps = read_input(sys.argv[1])
 	for i in range(len(inps)):
		(turn_around, sched_depart_a, sched_depart_b) = inps[i]
		
		# From the departure times, build a list of events, sorted in increasing
		# order of time:
		# [(t0, (station, event_kind)), (t1, station, event_kind)]
		# ti is a time in seconds since 00:00
		# station is 0 for A, 1 for b
		# event_kind is +1 for "train becomes available after turnaround"
		# event_kind is -1 for "train departs"
		#
		# So, build a complete list of these events from our input schedule
		
		events = []
		for da in sched_depart_a:
			ev2 = build_event(da, 0, 1, turn_around)
			events.append(ev2[0])
			events.append(ev2[1])
			
		for db in sched_depart_b:
			ev2 = build_event(db, 1, 0, turn_around)
			events.append(ev2[0])
			events.append(ev2[1])

		start_trains = [0, 0]
		trains = [0, 0]

		max_t = to_minutes('23:59')
		for e in sorted(events, cmp_keys):
			t = e[0]
			if t > max_t:
				break
				
			station = e[1][0]
			action = e[1][1]

#			print start_trains
#			print trains
#			print e
			
			if action == 1:	# another train becomes available here
				trains[station] += 1
			
			# @note: not elif!!! we can use a train as soon as it becomes available	
			if action == -1:	# we need to send a train, now
				# if we have a train, send it
				# if not, then we need another starting train at this station
				if not trains[station]:
					start_trains[station] += 1
					trains[station] += 1
					
				trains[station] -= 1
				
		# Processed all events. How many starting trains were needed?
		print "Case #%d: %d %d" % (i+1, start_trains[0], start_trains[1])

	
if __name__=='__main__':
  	main()
