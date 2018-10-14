#!/usr/bin/python

f = open("B-small.in")

def time_in_mins( t ):
	dd,mm = t.split(':')
	return 60*int(dd) + int(mm)

def get_time_list(num_trains):
	i = 0
	time_list = []
	for i in range(0,num_trains):
		start,end = f.readline().strip(nl).split(' ')
		start = time_in_mins(start)
		end = time_in_mins(end)
		time_list.append( (start,end) )
	return time_list


#f = open("input.txt")

nl = '\n'

num_cases = int(f.readline().strip(nl))

i = 0
for i in range(0,num_cases):
	a_times = []
	b_times = []
	to_a = []
	to_b = []
	cur_a = 0
	cur_b = 0
	start_a = 0
	start_b = 0

	turn = int(f.readline().strip(nl))

	ab,ba = f.readline().strip(nl).split(' ')
	ab = int(ab)
	ba = int(ba)
	
	a_trains = get_time_list(ab)
	b_trains = get_time_list(ba)
	a_trains.sort()
	b_trains.sort()
	#print a_trains
	#print b_trains
	
	while len(a_trains) > 0 or len(b_trains) > 0:
		cur_train = ()
		trains_at_station = 0
		proc_a = True
		to_a.sort()
		to_b.sort()
		
		take_a = True
		if len(a_trains) > 0:
			if len(b_trains) > 0:
				if a_trains[0] < b_trains[0]:
					take_a = True
				else:
					take_a = False
			else:
				take_a = True
		else:
			take_a = False
		
		if take_a == True:
			cur_train = a_trains.pop(0)
			trains_at_station = cur_a
			
			if len(to_a) > 0 and to_a[0] <= cur_train[0]:
				trains_at_station = trains_at_station + 1
				to_a.pop(0)
		else:
			cur_train = b_trains.pop(0)
			trains_at_station = cur_b
			proc_a = False

			if len(to_b) > 0 and to_b[0] <= cur_train[0]:
				trains_at_station = trains_at_station + 1
				to_b.pop(0)
		
		#print cur_train

		if trains_at_station == 0:
			trains_at_station = trains_at_station + 1
			if proc_a:
				start_a = start_a + 1
			else:
				start_b = start_b + 1
		
		#add train to other	
		if proc_a:
			to_b.append( cur_train[1] + turn )
			cur_a = trains_at_station - 1
		else:
			to_a.append( cur_train[1] + turn )
			cur_b = trains_at_station - 1
	
	output = "Case #" + str(i+1) + ": " + str(start_a) + " " + str(start_b)
	print output
