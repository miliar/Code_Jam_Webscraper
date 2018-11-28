def calc_solution(lines):
	solutions = []
	no_cases = long(lines[0])

	index = 1
	for case in range(0,no_cases):
		# Get first round
		solution_first_round = long(lines[index])-1
		index += 1
		card_numbers_first_round = [
			[ long(val) for val in line.split() ]
			for line in lines[index:index+4]
		]
		index += 4

		# Get first round
		solution_second_round = long(lines[index])-1
		index += 1
		card_numbers_second_round = [
			[long(val) for val in line.split()]
			for line in lines[index:index+4]
		]
		index += 4

		# Calculate solution. 
		# 0 means Bad Magician (multiple solutions).
		# -1 means volunteer cheated (no solutions).
		possible_values = [
			val for val in card_numbers_first_round[solution_first_round]
			if val in card_numbers_second_round[solution_second_round]
		]

		if len(possible_values) == 0:
			solutions.append("Volunteer cheated!")
		elif len(possible_values) > 1:
			solutions.append("Bad magician!")
		else:
			solutions.append(possible_values[0])

	return solutions


#########################################################

fin_name = 'A-small-attempt0.in'
fout_name = 'solution-A-small'

fin = open(fin_name,'r')
lines = [string.split("\n")[0] for string in fin.readlines()]

solutions = calc_solution(lines)

fout = open(fout_name,'w')
for i,solution in enumerate(solutions):
	fout.write("Case #%s: %s\n" % (i+1,solution))