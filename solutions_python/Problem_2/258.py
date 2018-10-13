import sys

import string

def get_pos(t):
	h,m = t.split(':')
	return int(h)*60 + int(m)
    
def sort_by_time(x, y):
	if x[0] > y[0]:
		# later times after earlier	 
		return 1
	elif x[0] < y[0]:
		# earlier times before later
		return -1
	elif x[1] and not y[1]:
		# departures come after arrivals
		return 1
	elif not x[1] and y[1]:
		# arrivals come before departures
		return -1
	else:
		# equal enough not to care
		return 1
		
f = open(sys.argv[1])
numProblems = int(f.readline())

for i in xrange(numProblems):
	turnaround = int(f.readline())
	tripcounts = f.readline().split()

	# each item is (time, isDeparture, stationInvolved)
	actions = []	
	for j in xrange(int(tripcounts[0])):
		start, end = f.readline().split()
		actions.append((get_pos(start), True, 'A'))
		actions.append((get_pos(end) + turnaround, False, 'B'))
	for j in xrange(int(tripcounts[1])):
		start, end = f.readline().split()
		actions.append((get_pos(start), True, 'B'))
		actions.append((get_pos(end) + turnaround, False, 'A'))
	actions.sort(sort_by_time)
	
	reserves = {'A':0, 'B':0}
	needed = {'A':0, 'B':0}
	
	for train in actions:
		isDeparture = train[1]
		station = train[2]
		if isDeparture:
			if reserves[station] > 0:
				reserves[station] -= 1
			else:
				needed[station] += 1
		else:
			reserves[station] += 1
	
	print 'Case #' + `i + 1` + ': ' + `needed['A']` + ' ' + `needed['B']`

	
	

    