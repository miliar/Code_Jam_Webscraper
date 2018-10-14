from pprint import pprint
import copy

infile = open('A-large.in', 'r')
#infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

num_problems = int(infile.readline())

def output(text):
	print(text)
	global outfile
	outfile.write("%s\n" % text)

def solve(vals):
	index = 0
	to_add = 0
	total = 0
	for i in vals:
		if total < index and i != 0:
			temp = to_add
			to_add = index - total + to_add
			total = total + to_add - temp
		total = total + i
		index = index + 1
	return to_add

for i in range(num_problems):
	max,vals = infile.readline().split(' ')
	vals = [int(x) for x in list(vals[:-1])]
	output("Case #%s: %s" % (i+1, solve(vals)))

infile.close()
outfile.close()

