# coding: shift-jis

import sys

f = file(sys.argv[1])

line_cnt = int(f.readline())

class Robot:
	def __init__(this):
		this.time     = 0
		this.position = 1

for number, s in enumerate(f):
	line = s.split()
	cnt = int(line[0])
	
	robots = {'O':Robot(), 'B':Robot()}
	
	time = 0
	
	for i in range(1, cnt+1):
		which  = line[2*i-1]
		button = int(line[2*i])
		
		r = robots[which]
		
		elapse   = time   - r.time
		distance = abs(button - r.position)
		
		if distance < elapse:
			time += 1
		else:
			time += distance - elapse + 1
			
		r.position = button
		r.time = time
	
	print 'Case #%d:'%(number+1), time
