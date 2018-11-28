import sys
import os
import re

def main():
	testcases = input()

	for test in range(0,testcases):
		inp = raw_input()
		spl = inp.split()

		cost=float(spl[0])
		accelration=float(spl[1])
		distance=float(spl[2])

		speed =2.0
		count =0.0

		fillig_time = cost/speed
		rest_time = (distance-cost)/speed
		total_time = fillig_time + rest_time
		
		while(1):
			count +=1
			next_speed = speed + (count*accelration)
			next_filling_time = fillig_time + cost/next_speed
			next_rest_time = (distance-cost)/next_speed
			next_total_time = next_rest_time+next_filling_time

			if(next_total_time> total_time):
				break
			else:
				fillig_time =next_filling_time
				total_time =next_total_time

		cases=test+1
		print 'Case #'+ str(cases) + ': ' +("%.7f" % total_time)
		
		test +=1	

if __name__ == "__main__":
	main()
