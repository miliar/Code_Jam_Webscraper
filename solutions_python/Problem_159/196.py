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

def method1(vals):
	prevval = vals[0]
	total = 0
	for val in vals:
		if val < prevval:
			total = total + prevval - val
		prevval = val
	return total
			
def method2(vals):
	max_decrease = 0
	for i in range(1,len(vals)):
		if vals[i-1] - vals[i] > max_decrease:
			max_decrease = vals[i-1] - vals[i]
	retval = max_decrease * (len(vals)-1)
	total = 0
	for i in range(0,len(vals)-1):
		total = total + min(vals[i],max_decrease)
	return total

for i in range(num_problems):
	infile.readline()
	vals = [int(x) for x in infile.readline().rstrip('\n').split(' ')]
	output("Case #%s: %s %s" % (i+1, method1(vals), method2(vals)))

infile.close()
outfile.close()

