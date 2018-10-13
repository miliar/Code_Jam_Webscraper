#!/usr/bin/python

C = int(raw_input())

for c in range(1,C+1):
	#print "Doing case %d" % (c)
	x = raw_input()
	vals = x.split(' ')
	n = int(vals[0])
	vals = vals[1:]
	for i in range(len(vals)):
		vals[i] = int(vals[i])
	
	#vals = sorted(vals)
	vals = sorted(list(set(vals)))
	smallest = vals[0]
	for i in range(len(vals)):
		vals[i] = vals[i] - smallest
	
	gaps = []
	for i in range(len(vals)-1):
		gaps = gaps + [vals[i+1] - vals[i]]
	
	gaps = sorted(gaps)
	sm_gap = gaps[0]
	#print gaps
	
	N = [1]
	Nf = 1
	for i in range(1, len(gaps)):
		#rem = (float(gaps[i]) / float(sm_gap)) - int(float(gaps[i]) / float(sm_gap))
		#space = 1.0 - rem
		#print "space is %f" % (space)
		#this_N = round(1.0 / space)
		#N = N + [ this_N ]
		upper = gaps[i]
		lower = sm_gap
		#print "Upper %d lower %d" % (upper, lower)
		if upper % lower == 0:
			N = N + [1]
			continue
		this_N = 2
		while True:
			if (upper % (lower/this_N) == 0) and (lower % this_N == 0):
				N = N + [ this_N ]
				break
			this_N = this_N + 1
			# Oh balls
#			if (this_N > 100000):
#				N = N + [ lower ]
#				break
		#print "Found N = %d" % this_N

	
	#print N
	
	N = sorted(list(set(N)))
	
	for i in range(len(N)):
		adding = True
		while adding == True:
			adding = False
			if ((Nf) % N[i]) != 0:
				Nf = (int((Nf/N[i])) + 1)*N[i]
				for j in range(i):
					if (Nf % N[j]) != 0:
						adding = True
						break
	#print "Sm_gap:"
	#print sm_gap
	#print "Nf:"
	#print Nf
	
	best_gap = int(float(sm_gap) / float(Nf));
	#print "Best gap:"
	#print best_gap
	#print (int(float(smallest) / best_gap) + 1)
	#print int(9 * best_gap)
	abs_time = int(round((int((smallest) / best_gap) + 1) * best_gap))
	if abs_time == smallest + best_gap:
		abs_time = smallest
	#print abs_time
	delay = abs_time - smallest
	#print delay
	
	print "Case #%d: %ld" % (c, delay)
	
