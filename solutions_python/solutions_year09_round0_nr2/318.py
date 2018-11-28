#!/usr/bin/python
import string
import re
def read_input():
	file = open("input.in")
	lines = file.readlines()
	file.close()
	return lines

def write_output(lines):
	file = open("output.out", "w")
	file.writelines(lines)
	file.close()

def get_sink(basin, loc):
	currentHeight = basin[loc[0]][loc[1]]
	neighbors = [(loc[0] - 1, loc[1]),\
			(loc[0], loc[1] - 1),\
			(loc[0], loc[1] + 1),\
			(loc[0] + 1, loc[1])]
	bestN = None
	bestNHeight = currentHeight
	for n in neighbors:
		if 0 <= n[0] < len(basin) and 0 <=n[1] < len(basin[0]):
			if basin[n[0]][n[1]] < bestNHeight:
				bestN = n
				bestNHeight = basin[n[0]][n[1]]
	if not bestN:
		return loc
	return get_sink(basin, bestN)

if __name__=="__main__":
	input = read_input()
	num_cases = int(input[0])
	case_start = 1
	output = []
	for case_index in range(num_cases):
		num_rows = int(input[case_start].split(" ")[0])
		basin = []
		for row in input[case_start+1:case_start+1+num_rows]:
			basin.append([int(i) for i in row.split(" ")])
		case_start += 1 + num_rows
		#Generate array of sink locations for each cell in the basin
		basin_sinks = []
		for rindex, row in enumerate(basin):
			row_sinks = []
			for cindex, col in enumerate(row):
				row_sinks.append(get_sink(basin, (rindex, cindex)))
			basin_sinks.append(row_sinks)
		#Generate array of coded basin regions
		pallate = list("abcdefghijklmnopqrstuvwxyz")
		#maps basins (by sink location tuple) to letters from the pallate
		usedLetters = {}
		basin_final = []
		for row in basin_sinks:
			row_final = []
			for col in row:
				if usedLetters.has_key(col):
					row_final.append(usedLetters[col])
				else:
					usedLetters[col] = pallate.pop(0)
					row_final.append(usedLetters[col])
			basin_final.append(row_final)
		output.append("Case #" + str(case_index + 1) + ":\n")
		for row in basin_final:
			output.append(" ".join([str(i) for i in row]) + "\n")
	write_output(output)
