#!/usr/bin/python
import sys

def read_grid(lines, i):
	output = {}
	for x in range(4):
		output[x] = lines[i+x].split(" ")
	return output

f = open(sys.argv[1], 'r')
inputs = f.read()

lines = inputs.split('\n')
total_cases = lines[0]
i = 1
for case in range(int(total_cases)):
	chosen1 = lines[i]
	i += 1
	layout1 = read_grid(lines, i)
	set1 = layout1[int(chosen1) - 1]
	i += 4
	chosen2 = lines[i]
	i += 1
	layout2 = read_grid(lines, i)
	set2 = layout2[int(chosen2) - 1]
	i += 4

	intersection = []
	for num in set1:
		if num in set2:
			intersection.append(num)

	output = "Case #" + str(case+1) + ": "
	if len(intersection) == 0:
		output += "Volunteer cheated!"
	elif len(intersection) == 1:
		output += intersection[0]
	else:
		output += "Bad magician!"

	print output
