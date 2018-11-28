import sys
from math import floor, ceil, sqrt

input = open(sys.argv[1], "r").readlines()#[1:]
output = open(sys.argv[2], "w")

def parse(lines):
	def inner_parse(line):
		while True:
			first_answer = int(line)
			line = yield
			arrangements = [[], []]
			for i in range(4):
				arrangements[0].append(set(map(int, line.split(" "))))
				line = yield
			second_answer = int(line)
			line = yield
			for i in range(4):
				arrangements[1].append(set(map(int, line.split(" "))))
				if not i == 3:
					line = yield
			line = (yield {
				"first_answer": first_answer,
				"arrangements": arrangements,
				"second_answer": second_answer
			})
		
	parser = inner_parse(lines[0])
	next(parser)
	for raw_line in lines[1:]:
		output = parser.send(raw_line)
		if output is None:
			continue
		yield output
	
for (i, state) in enumerate(parse(input[1:])):
	result = list(state["arrangements"][0][state["first_answer"]-1].intersection(state["arrangements"][1][state["second_answer"]-1]))
	if len(result) == 1:
		output.write("Case #" + str(i+1) + ": " + str(result[0]) + "\n")
	elif len(result) > 1:
		output.write("Case #" + str(i+1) + ": " + "Bad magician!" + "\n")
	else:
		output.write("Case #" + str(i+1) + ": " + "Volunteer cheated!" + "\n")