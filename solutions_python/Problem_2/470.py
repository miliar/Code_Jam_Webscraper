#!/usr/bin/env python

debug = False


def get_time(time_str):
	time_list = time_str.split(":")
	hh = int(time_list[0])
	mm = int(time_list[1])
	return hh*60 + mm


if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		filename = sys.argv[1]

	else:
		infile = "B-small.in"
	infile = open(filename, "r")


	num_cases = int( infile.readline() )
	for case in range(num_cases):

		if debug:
			print "Case", case+1
			print "~"*40


		turnaround_minutes = int( infile.readline() )

		NA, NB = tuple([int( num ) for num in infile.readline().split()])

		min_A_trains, min_B_trains = (0, 0)
		A_trains, B_trains = (0, 0)

		# both lists sorted by departure time in increasing order
		a_arrivals = []
		a_departures = []
		b_arrivals = []
		b_departures = []

		if debug:
			max_arrival_time_either_way = 0

		for trip_a_to_b in range(NA):
			line = infile.readline()
			departure_time, arrival_time = tuple([get_time(time) for time in line.split()])
			a_departures.append( departure_time )
			b_arrivals.append( arrival_time + turnaround_minutes )
			if debug:
				max_arrival_time_either_way = max(arrival_time, max_arrival_time_either_way)


		a_departures.sort()
		b_arrivals.sort()


		for trip_b_to_a in range(NB):
			line = infile.readline()
			departure_time, arrival_time = tuple([get_time(time) for time in line.split()])
			b_departures.append( departure_time )
			a_arrivals.append( arrival_time + turnaround_minutes )
			if debug:
				max_arrival_time_either_way = max(arrival_time, max_arrival_time_either_way)

		b_departures.sort()
		a_arrivals.sort()

		if debug:
			print "A departures:", a_departures
			print "A arrivals:", a_arrivals

			print "B departures:", b_departures
			print "B arrivals:", b_arrivals

			print "~"*40

		a_arrival_index = 0
		for departure_time in a_departures:

			while a_arrival_index < len(a_arrivals) and a_arrivals[a_arrival_index] <= departure_time:
				A_trains += 1
				if debug:
					print "Increasing A_trains count to", A_trains, "at", a_arrivals[a_arrival_index]
				a_arrival_index += 1

			A_trains -= 1
			min_A_trains = min(A_trains, min_A_trains)
			if debug:
				print "Decreasing A_trains count to", A_trains, "at", departure_time, "-- New min:", min_A_trains

		if debug:
			print '='*80


		b_arrival_index = 0
		for departure_time in b_departures:

			while b_arrival_index < len(b_arrivals) and b_arrivals[b_arrival_index] <= departure_time:
				B_trains += 1
				if debug:
					print "Increasing B_trains count to", B_trains, "at", b_arrivals[b_arrival_index]
				b_arrival_index += 1

			B_trains -= 1
			min_B_trains = min(B_trains, min_B_trains)
			if debug:
				print "Decreasing B_trains count to", B_trains, "at", departure_time, "-- New min:", min_B_trains


		print "Case #%d: %d %d" % (case+1, -min_A_trains, -min_B_trains)


		if debug:
			print '*'*80
			print '*'*80

	if debug:
		print "max_arrival_time_either_way:", max_arrival_time_either_way
