#!/usr/bin/env python


import sys


def problem_A(filename, outfile=None):
	try:
		if not os.path.exists(outfile):
			output = open(outfile, "w")
	except:
		output = None
	with open(filename, "r") as f:
		num_cases = int(f.readline())
		#print num_cases
		for n in xrange(num_cases):
			first_answer = int(f.readline().strip())
			#print first_answer
			first_rows = [map(lambda x: int(x), f.readline().strip().split(" ")) for _ in xrange(4)]
			second_answer = int(f.readline().strip())
			second_rows = [map(lambda x: int(x), f.readline().strip().split(" ")) for _ in xrange(4)]
			possibles = set(first_rows[first_answer-1]).intersection(set(second_rows[second_answer-1]))
			if len(possibles) < 1:
				answer = "Volunteer cheated!"
			elif len(possibles) > 1:
				answer = "Bad magician!"
			else:
				answer = list(possibles)[0]

			line = "Case #" + str(n+1) + ": " + str(answer)
			if output:
				output.write(line + "\n")
			print line


if __name__ == "__main__":
	try:
		filename = sys.argv[1]
		try:
			outfile = sys.argv[2]
		except IndexError:
			outfile = None	
		problem_A(filename, outfile)
	except IndexError:
		print "Usage:\n"
		print "\t" + sys.argv[0] + " filename [outfile]"


