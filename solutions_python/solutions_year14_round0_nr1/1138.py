import sys

filename = "A-small-attempt1"

def solve_case(case, first_ans, first_arrange, second_ans, second_arrange):

	first_set = set(first_arrange[first_ans-1])
	second_set = set(second_arrange[second_ans-1])
	possibilities = 0
	match_card = 0
	for card in first_set:
		if card in second_set:
			possibilities += 1
			match_card = card
	if possibilities == 0:
		output = "Volunteer cheated!"
	elif possibilities == 1:
		output = match_card
	else:
		output = "Bad magician!"
	ret = "Case #%s: %s" % (case+1, output)
	return ret

def readInt(inFile):
	return int(inFile.readline())

def readFloats(inFile):
	return [int(n) for n in inFile.readline().split(" ")]

def readInts(inFile):
	return [int(n) for n in inFile.readline().split(" ")]

with open(filename + ".in", 'r') as inFile:
	output_data = []

	# parse input
	T = readInt(inFile)
	for t in range(T):
		first_ans = readInt(inFile)
		first_arrange = [readInts(inFile) for i in range(4)]
		second_ans = readInt(inFile)
		second_arrange = [readInts(inFile) for i in range(4)]
		soln = solve_case(t, first_ans, first_arrange, second_ans, second_arrange)
		output_data.append(soln)

	if len(output_data) > 0:
		with open(filename + ".out", 'w') as outFile:
			outFile.write("\n".join(output_data))
	else:
		print("no output")




