#!/usr/bin/python

n_cases = int(raw_input(""))

for icase in range(0,n_cases):
	#print "-START CASE-"
	turnaroundtime = int(raw_input(""))
	na, nb = (raw_input("")).strip().split(" ")

	na = int(na)
	nb = int(nb)
	timeline_a = []
	timeline_b = []
	for na_i in xrange(0,na):
		stime_start, stime_end = raw_input("").strip().split(" ")
		shr,smin = stime_start.split(":")
		ehr ,emin = stime_end.strip().split(":")
		sched = []
		sched.append(int(shr)*60 + int(smin) )
		sched.append(int(ehr)*60 + int(emin) )
		timeline_a.append(sched)
	for nb_i in xrange(0,nb):
		stime_start, stime_end = raw_input("").strip().split(" ")
		shr,smin = stime_start.split(":")
		ehr ,emin = stime_end.strip().split(":")
		sched = []
		sched.append(int(shr)*60 + int(smin) )
		sched.append(int(ehr)*60 + int(emin) )
		timeline_b.append(sched)
	#print timeline_a
	#print timeline_b
	
	# -- basic sorting
	
	f = True
	while f:
		f = False
		for i in xrange(0,len(timeline_a)-1):
			if timeline_a[i][0] > timeline_a[i+1][0]:
				t = timeline_a[i] 
				timeline_a[i] = timeline_a[i+1]
				timeline_a[i+1] = t
				f = True
	f = True
	while f:
		f = False
		for i in xrange(0,len(timeline_b)-1):
			if timeline_b[i][0] > timeline_b[i+1][0]:
				t = timeline_b[i] 
				timeline_b[i] = timeline_b[i+1]
				timeline_b[i+1] = t
				f = True
	#print "Aftersort:", timeline_a
	#print timeline_b
	# -- done reading now some processing
	
	route_a = 0 
	route_b = 0
	avail_a = 0
	avail_b = 0
	curtime = 0
	alen = range(0,len(timeline_a))
	blen = range(0,len(timeline_b))
	while curtime < 86400:
		for ib in blen:
			if timeline_b[ib][1] + turnaroundtime == curtime:
				avail_a = avail_a + 1
		for ia in alen:
			if timeline_a[ia][1] + turnaroundtime == curtime:
				avail_b = avail_b + 1
		req_a = 0 
		req_b = 0
		for ia in alen:
			if timeline_a[ia][0] == curtime:
				req_a = req_a + 1
		for ib in blen:
			if timeline_b[ib][0] == curtime:
				req_b = req_b + 1
		avail_a = avail_a - req_a
		avail_b = avail_b - req_b
		if avail_a < 0:
			route_a = route_a - (avail_a)
			avail_a = 0
		if avail_b < 0:
			route_b = route_b - (avail_b)
			avail_b = 0
		curtime = curtime + 1
		#print curtime , "\r" ,
	print ("Case #%d: %d %d") % (icase+1, route_a, route_b)
