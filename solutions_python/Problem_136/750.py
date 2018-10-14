"""Code written using Python 2.7.5, http://www.python.org/"""
import math

def getTotalTime(farmprice, farmrate, x, numfarms):
	rate = 2.0
	seconds = 0.0
	if numfarms > 0:
		for i in range(0, numfarms):
			seconds += farmprice / rate
			rate += farmrate

	seconds += x / rate
	return seconds


def calc(case):
	#print "**************************************"
	#print "Case:", case
	#print "**************************************"

	(farmprice, farmrate, x) = [float(e) for e in case.split()]

	farmmin = 0
	farmmax = int(math.ceil(x))
	while True:
		numfarms = (farmmax-farmmin) / 2 + farmmin
		newtime = getTotalTime(farmprice, farmrate, x, numfarms)
		timeplus = getTotalTime(farmprice, farmrate, x, numfarms + 1)
		timeminus = getTotalTime(farmprice, farmrate, x, numfarms - 1)
		#print "Numfarms:", numfarms, "time:", newtime, "timeplus:", timeplus, "timeminus:", timeminus
		if newtime <= timeplus and newtime <= timeminus:
			time = newtime
			break
		elif newtime < timeplus and newtime > timeminus:
			farmmax = numfarms
			time = newtime
		elif newtime > timeplus and newtime < timeminus:
			farmmin = numfarms
			time = newtime


			


	return time


		
		
def main():
	f = open('B-large.in', 'r')
	lines = f.readlines()
	f.close()
	c = lines[0].split()[0]
	#print c
	lines = [r.strip() for r in lines[1:]]
	#print cases

	of = open('output_b_large.txt', 'w')

	for idx, case in enumerate(lines):
		of.write('Case #%(idx)i: %(i).7f\n' % {'idx': idx + 1, 'i': calc(case)})

	of.close()

main()
#import timeit
#print timeit.timeit("main()", setup="from __main__ import main", number=1)
