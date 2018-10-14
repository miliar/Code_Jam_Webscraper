#!/usr/bin/python

import sys

def unzip(schedule):
	departures = [None] * len(schedule)
	arrives = [None] * len(schedule)
	for i in xrange(len(schedule)):
		departures[i] = schedule[i][0]
		arrives[i] = schedule[i][1]
	return departures, arrives

def how_many_trains(turn_around, AB_schedule, BA_schedule):

	AB_departures, AB_arrives = unzip(AB_schedule)
	BA_departures, BA_arrives = unzip(BA_schedule)
	AB_trains = minimize_train(turn_around, AB_departures, BA_arrives)
	BA_trains = minimize_train(turn_around, BA_departures, AB_arrives)
	return str(AB_trains) + " " + str(BA_trains)

def minimize_train(turn_around, AB_departures, BA_arrives):
	AB_departures.sort()
	BA_arrives.sort()
	trains_needed = len(AB_departures)
	for x in AB_departures:
		for y in xrange(len(BA_arrives)):
			if x >= BA_arrives[y] + turn_around:
				BA_arrives.pop(y)
				trains_needed -= 1
				break
	return trains_needed

def time_in_minute(time_in_clock_format):
	hour, minute = time_in_clock_format.split(":")
	return int(hour) * 60 + int(minute)

def render(schedule):
	departure, arrive = schedule.split()
	return time_in_minute(departure), time_in_minute(arrive)

def main():
	istream = sys.stdin
	cases = int(istream.readline())
	for case in xrange(cases):
		turn_around = int(istream.readline())
		AB_trips_num, BA_trips_num = istream.readline().split()
		AB_trips_num, BA_trips_num = int(AB_trips_num), int(BA_trips_num)
		AB_schedule = [None] * AB_trips_num
		BA_schedule = [None] * BA_trips_num
		for AB in xrange(AB_trips_num):
			AB_schedule[AB] = render(istream.readline())
		for BA in xrange(BA_trips_num):
			BA_schedule[BA] = render(istream.readline())

		case_output = how_many_trains(turn_around,
					AB_schedule, BA_schedule)
		print "Case #%s: %s" % (case+1, case_output)

if __name__ == "__main__":
	exit_status = main()
	sys.exit(exit_status)
