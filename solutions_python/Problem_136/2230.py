#!/usr/bin/env python


import os
import sys


def problem_B(filename, outfile=None):
	try:
		if not os.path.exists(outfile):
			output = open(outfile, "w")
	except:
		output = None
	with open(filename, "r") as f:
		"""
		Track the number of seconds it takes to 
		"""
		num_cases = int(f.readline())
		#print num_cases
		for n in xrange(num_cases):
			C, F, X = map(float, f.readline().strip().split(" "))

			times = []
			rate = 2.0
			min_time = 0.0
			while True:
				max_time = min_time + (X / rate)

				min_time += C / rate
				rate += F

				if len(times) > 0 and times[-1] < max_time:
					break
				else:
					times.append(max_time)


			#print times
			answer = times[-1]

			# print answer
			line = "Case #" + str(n+1) + ": " + "{:10.7f}".format(answer)
			print line
			if output:
				output.write(line + "\n")


if __name__ == "__main__":
	try:
		filename = sys.argv[1]
		try:
			outfile = sys.argv[2]
		except IndexError:
			outfile = None	
		problem_B(filename, outfile)
	except IndexError:
		print "Usage:\n"
		print "\t" + sys.argv[0] + " filename [outfile]"


