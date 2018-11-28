#!/bin/python

#a_avail = {}
#b_avail = {}

def getline():
	return f.readline().strip()

def log(msg):
#	print msg
	return

def parse_trip_line(line):
	start, end = line.split()
	start = int(start.replace(':', ''))
	end = int(end.replace(':', ''))
	return (start, end)

def train_needed(station_avail, time):
	if time in station_avail:
		station_avail[time] -= 1
	else:
		station_avail[time] = -1

def train_ready(station_avail, time):
	if time in station_avail:
		station_avail[time] += 1
	else:
		station_avail[time] = 1

def get_min(station_avail):
	# Sort by time
	times = station_avail.keys()
	times.sort()
	avail_total = 0
	min = 0
	log("Finding min avail trains")
	for t in times:
		avail_total += station_avail[t]
		log(avail_total)
		if avail_total < min:
			min = avail_total
	log("Min: %d" % min)
	return min

def do_case(case_num):
	"""case_num 1 based."""
	a_avail = {}
	b_avail = {}
	turnaround = int(getline())
	line = getline().split()
	a_to_b_trips = int(line[0])
	b_to_a_trips = int(line[1])
	log("%d, %d, %d" % (turnaround, a_to_b_trips, b_to_a_trips))
	log("a to b trips:")
	for i in range(a_to_b_trips):
		start, end = parse_trip_line(getline())
		log("start: %d, end: %d" % (start, end))
		ready = end + turnaround
		train_needed(a_avail, start)
		train_ready(b_avail, ready)
	log("b to a trips:")
	for i in range(b_to_a_trips):
		start, end = parse_trip_line(getline())
		log("start: %d, end: %d" % (start, end))
		ready = end + turnaround
		train_needed(b_avail, start)
		train_ready(a_avail, ready)
	
	log("a_avail: %s" % a_avail)
	log("b_avail: %s" % b_avail)
	
	a_min = get_min(a_avail)
	b_min = get_min(b_avail)
	
	print "Case #%d: %d %d" % (case_num, -a_min, -b_min)

def main():
	global f
	f = open('B-small-attempt0.in')
	cases = int(getline())
	log("%d cases" % cases)
	for case in range(cases):
		do_case(case + 1)

main()
