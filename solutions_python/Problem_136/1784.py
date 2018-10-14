#!/usr/bin/python

#fin = open('cookie-sample.txt')
fin = open('B-small-attempt0.in')
inputline = fin.readline()
numcase = int(inputline)

fout = open('cookie_sample_small.txt', 'w')


def calc_time(numfac, cost, oldrate, boost, goal):
	timereq = 0
	facleft = numfac
	rate = oldrate
	while (facleft > 0):
		factory_time = cost / rate
		timereq += factory_time
		rate += boost
		facleft = facleft - 1
	timetogoal = goal/rate
	timereq += timetogoal 
	return timereq

for i in range (1,numcase+1):
	line = fin.readline()
	linelist = line.split()
	c = float(linelist[0])
	f = float(linelist[1])
	x = float(linelist[2])
	zerofac = x/2
	roi_time = c/f
	single_cost = c/2
	#print "#i="+str(i)+" CostFactory="+str(c)+" F="+str(f) +" XGoal="+str(x)
	#print "ROI time ="+str(roi_time)
	if (x < c) or (zerofac < single_cost+roi_time):
		answer = x/2
	else:
		optimal = False
		oldrate = 2
		newrate = 2+f
		best = zerofac
		numfac = 1
		while (not optimal):
			newtime = calc_time(numfac, c,oldrate, f, x)
			if newtime < best:
				answer = newtime
				best = newtime
				numfac +=1
				#oldrate = newrate
				#newrate = oldrate + f
			else:
				answer = best
				optimal = True



	answer_out = "Case #"+str(i)+": "+str(answer)+"\n"
	fout.write(answer_out)
	print answer_out