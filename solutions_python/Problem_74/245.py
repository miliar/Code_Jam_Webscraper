#!/usr/bin/python

fp = open('A-large.in')

fp.readline()
c = 1

for line in fp:
	line = line[:-1]
	arr = line.split(' ')
	arr = arr[1:]
	oPos = 1
	bPos = 1
	ttime = 0	
	time = len(arr)/2 * [0]
	sofar = 0
	lastseen = None
	
	for i in range(len(arr)/2):
		robot = arr[i*2]
		dist = int(arr[i*2+1])
		
		if robot == "O":
			tm = abs(dist-oPos)+1
			oPos = dist
			time[i] = tm
			if lastseen == "B":
				if sofar >= tm:
					time[i] = 1
				else:
					time[i] = tm - sofar 
				sofar = 0
			sofar = sofar + time[i]			
			lastseen = "O"
		elif robot == "B":
			tm = abs(dist-bPos)+1
			bPos = dist
			time[i] = tm
			if lastseen == "O":
				if sofar >= tm:
					time[i] = 1
				else:
					time[i] = tm - sofar 
				sofar = 0
			sofar = sofar + time[i]
			lastseen = "B"
	
	for i in time:
		ttime = ttime + i
	print "Case #%d: %d" % (c,ttime)
	c = c + 1
