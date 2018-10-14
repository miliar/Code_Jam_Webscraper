#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

def to_minutes(time):
	try: 
		return int(time)
	except:	
		tmp = time.split(':')
		return int(tmp[0])*60 + int(tmp[1])
	
def get_train_in_stations(station, time):
	target = to_minutes(time)
	last_total_train = 0
	times = stations[station].keys()
	times.sort()
	for minute in times:
		total_train = stations[station][minute]
		last_total_train = total_train
		if minute == target:
			return total_train
		elif minute >= target:
			return last_total_train
	return last_total_train
	
def leave(station, time):
	leave_time = to_minutes(time)
	trains = get_train_in_stations(station, time)
	if trains == 0:
		need_trains[station] = need_trains[station] + 1
		# print "buy train at ", station
		trains = 1
	stations[station][leave_time] = trains - 1
	
def arrive(station, time):
	ready_time = to_minutes(time)
	stations[station][ready_time] = get_train_in_stations(station, ready_time) + 1

def process(time_tables):
	global stations
	global need_trains
	stations = [{}, {}]
	need_trains = [0,0]
	times = time_tables.keys()
	times.sort()
	for time in times:
		events = time_tables[time]
		events.sort()
		for event in events:
			if event == 'arrive a':
				arrive(0, time)
			elif event == 'arrive b':
				arrive(1, time)
			elif event == 'leave a':
				leave(0, time)
			elif event == 'leave b':
				leave(1, time)
			
	return need_trains

def add_event(time_tables, time, event):
	if time not in time_tables:
		time_tables[time] = []
	time_tables[time].append(event)
	
def main():
	f = sys.stdin
	
	cases = int(f.readline())
	for j in range(cases):
		offset = int(f.readline())
		tmp = f.readline().split(' ')
		a_to_b = int(tmp[0])
		b_to_a = int(tmp[1])
		time_tables = {}
		for i in range(a_to_b):
			tmp = f.readline().split(' ')
			add_event(time_tables, to_minutes(tmp[0]), 'leave a')
			add_event(time_tables, to_minutes(tmp[1])+offset, 'arrive b')
			
		for i in range(b_to_a):
			tmp = f.readline().split(' ')
			add_event(time_tables, to_minutes(tmp[0]), 'leave b')
			add_event(time_tables, to_minutes(tmp[1])+offset, 'arrive a')
		
		result = process(time_tables)
		print "Case #" + str(j+1) + ":", result[0], result[1]
	f.close()

if __name__ == '__main__':
	sys.exit(main())


