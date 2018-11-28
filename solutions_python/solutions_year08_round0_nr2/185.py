def timetomins(t):
	hours, minutes = t.split(':')
	return int(hours) * 60 + int(minutes)

def key_compare(x, y):
	return x[0] - y[0]

def best_train(trains, needed_time):
	#trains already reverse sorted
	for train in trains:
		if train <= needed_time:
			return train
	#print str(trains) + ' needed: ' + str(needed_time)
	return -1 #none available

def timetable(turntime, na, nb, ab_trips, ba_trips):
	inita_trains = 0
	initb_trains = 0
	a_trains = [ ] # time available at
	b_trains = [ ]
	ab_trips.sort(cmp = key_compare)
	ba_trips.sort(cmp = key_compare)
	#print 'a->b: ' + str(ab_trips)
	#print 'a<-b: ' + str(ba_trips)
	# no trips other way
	if na == 0:
		return '0 ' + str(nb)
	if nb == 0:
		return str(na) + ' 0'
	for i in xrange(max(na, nb)):
		a_trains.sort()
		a_trains.reverse()
		b_trains.sort()
		b_trains.reverse()
		if i > na - 1: # making an BA trip only (no more AB)
			#print 'ba only'
			if best_train(b_trains, ba_trips[i][0]) == -1: # no train available
				b_trains.append(0) # available immeditely
				initb_trains += 1
			b_trains.remove(best_train(b_trains, ba_trips[i][0]))
			a_trains.append(ba_trips[i][1] + turntime)
		elif i > nb - 1: #AB
			#print 'ab only'
			if best_train(a_trains, ab_trips[i][0]) == -1:
				a_trains.append(0)
				inita_trains += 1
			a_trains.remove(best_train(a_trains, ab_trips[i][0]))
			b_trains.append(ab_trips[i][1] + turntime)
		else:
			if ab_trips[i][0] < ba_trips[i][0]:
				#print 'ab first'
				if best_train(a_trains, ab_trips[i][0]) == -1:
					a_trains.append(0)
					inita_trains += 1
				a_trains.remove(best_train(a_trains, ab_trips[i][0]))
				b_trains.append(ab_trips[i][1] + turntime)
				a_trains.sort()
				a_trains.reverse()
				b_trains.sort()
				b_trains.reverse()
				if best_train(b_trains, ba_trips[i][0]) == -1: # no train available
					b_trains.append(0) # available immeditely
					initb_trains += 1
				b_trains.remove(best_train(b_trains, ba_trips[i][0]))
				a_trains.append(ba_trips[i][1] + turntime)
			elif ab_trips[i][0] > ba_trips[i][0]:
				#print 'ba first'
				if best_train(b_trains, ba_trips[i][0]) == -1: # no train available
					b_trains.append(0) # available immeditely
					initb_trains += 1
				b_trains.remove(best_train(b_trains, ba_trips[i][0]))
				a_trains.append(ba_trips[i][1] + turntime)
				a_trains.sort()
				a_trains.reverse()
				b_trains.sort()
				b_trains.reverse()
				if best_train(a_trains, ab_trips[i][0]) == -1:
					a_trains.append(0)
					inita_trains += 1
				a_trains.remove(best_train(a_trains, ab_trips[i][0]))
				b_trains.append(ab_trips[i][1] + turntime)
			else:
				if ab_trips[i][1] < ba_trips[i][1]:
					#print 'ab first'
					if best_train(a_trains, ab_trips[i][0]) == -1:
						a_trains.append(0)
						inita_trains += 1
					a_trains.remove(best_train(a_trains, ab_trips[i][0]))
					b_trains.append(ab_trips[i][1] + turntime)
					a_trains.sort()
					a_trains.reverse()
					b_trains.sort()
					b_trains.reverse()
					if best_train(b_trains, ba_trips[i][0]) == -1: # no train available
						b_trains.append(0) # available immeditely
						initb_trains += 1
					b_trains.remove(best_train(b_trains, ba_trips[i][0]))
					a_trains.append(ba_trips[i][1] + turntime)
				else:
					#print 'ba first'
					if best_train(b_trains, ba_trips[i][0]) == -1: # no train available
						b_trains.append(0) # available immeditely
						initb_trains += 1
					b_trains.remove(best_train(b_trains, ba_trips[i][0]))
					a_trains.append(ba_trips[i][1] + turntime)
					a_trains.sort()
					a_trains.reverse()
					b_trains.sort()
					b_trains.reverse()
					if best_train(a_trains, ab_trips[i][0]) == -1:
						a_trains.append(0)
						inita_trains += 1
					a_trains.remove(best_train(a_trains, ab_trips[i][0]))
					b_trains.append(ab_trips[i][1] + turntime)
	return str(inita_trains) + ' ' + str(initb_trains)

n = int(raw_input())
output = ''
for x in xrange(1, n+1):
	turntime = int(raw_input())
	na, nb = raw_input().split(' ')
	na, nb = int(na), int(nb)
	ab_trips = [ ]
	ba_trips = [ ]
	for y in xrange(na):
		depart, arrive = raw_input().split(' ')
		depart, arrive = timetomins(depart), timetomins(arrive)
		ab_trips.append((depart, arrive))
	for y in xrange(nb):
		depart, arrive = raw_input().split(' ')
		depart, arrive = timetomins(depart), timetomins(arrive)
		ba_trips.append((depart, arrive))
	output += 'Case #' + str(x) + ': ' + timetable(turntime, na, nb, ab_trips, ba_trips) + '\n'
print '\n' + output