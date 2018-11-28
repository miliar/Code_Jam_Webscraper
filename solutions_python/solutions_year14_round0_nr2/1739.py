"""
Chad Reynolds 4/11/14

Google Code Jam 2014
Qualifying Round
Problem B

Elapsed time from beginning to submission:  
"""
import sys

def readfile_lines(filename):
	"""Reads in the given file, then returns every line of text(minus the number of lines) as a list."""

	file = open(filename, "r")
	num_lines = int(file.readline())
	text = []
	for i in range(num_lines):
		text.append(file.readline().rstrip().split(" "))
	file.close()
	return text

def readfile_bulk(filename):
	"""Reads in the given file as a single large string without any formatting."""

	file = open("filename", "r")
	return file.read()

if __name__ == "__main__":

	input = sys.argv[1]
	output = sys.argv[2]

	text = readfile_lines(input)	
	output = open(output, "w")

	## problem ##
	for i in range(len(text)):
		answer = 0.0
		initial_rate = 2.0
		farm_cost = float(text[i][0])
		cookie_bonus = float(text[i][1])
		goal_cookies = float(text[i][2])

		found = False
		rate = initial_rate
		time = goal_cookies / rate
		bought = 0

		while not found:
			bought += 1
			rate = initial_rate
			next_time = 0.0
			for j in range(bought):
				next_time += farm_cost / rate
				rate += cookie_bonus		
			next_time += goal_cookies / rate		
			
			if next_time > time:
				found = True
			else:
				time = next_time
			#print("Case {0}>>  Bought: {1}  Time:  {2}  Found:  {3}".format(i+1, bought, time, found))
		
		answer = time
		# output answer
		print("Case {0} answer is {1} with {2} farms".format(i+1, answer, bought))
		output.write("Case #{0}: {1}\n".format(i+1, answer))

	output.close()	
