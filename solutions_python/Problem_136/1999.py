import sys
from math import floor, ceil, sqrt

input = open(sys.argv[1], "r").readlines()#[1:]
output = open(sys.argv[2], "w")

def parse(lines):
	def inner_parse(line):
		arrangement = []
	for raw_line in lines:
		line = raw_line.strip().split(" ")
		output = (float(line[0]), float(line[1]), float(line[2]))
		yield output
		
def remaining(cookies, F, bought, base_rate, X):
	return float(X-cookies)/float(F*bought + 2)
		
for (i, (C, F, X)) in enumerate(parse(input[1:])):
	bought = 0
	base_rate = 2
	time = C/base_rate
	cookies = base_rate*time
	complete = cookies > X
	while not complete:
		buy_it = remaining((cookies-C), F, bought+1, base_rate, X)
		skip_it = remaining((cookies), F, bought, base_rate, X)
		if buy_it < skip_it:
			bought += 1
			cookies -= C
			delta = C/(bought*F + base_rate)
			complete = False
		else:
			delta = (X-cookies)/(bought*F + base_rate)
			complete = True
		# update values, advance to the next possible purchase block
		time += delta
		cookies += delta*(bought*F + base_rate)
	result = time - float(abs(cookies-X))/(base_rate+bought*F)
	output.write("Case #" + str(i+1) + ": " + str(result) + "\n")