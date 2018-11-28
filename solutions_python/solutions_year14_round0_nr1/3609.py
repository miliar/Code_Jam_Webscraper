#A: MAGIC TRICK

prob_file = open('A-small-attempt0.in', 'r')#open the file containing the problems

out_file = open('out.txt', 'w')

lines = []
for line in prob_file:
	lines.append(line)
	
num_cases = lines[0]

lines_per = 10

for i in range(1, len(lines), lines_per):
	case_lines = lines[i:i+lines_per]
	first_guess = int(case_lines[0])
	first_grid = case_lines[1:5]
	
	second_guess = int(case_lines[5])
	second_grid = case_lines[6:10]
	
	first_guess_row = first_grid[first_guess-1].split()
	
	second_guess_row = second_grid[second_guess-1].split()
	
	
	possible_solutions = []
	for j in first_guess_row:
		for k in second_guess_row:
			if k==j:
				possible_solutions.append(j)
				
	print possible_solutions
	
	case_num = 'Case #'+str((i/10)+1)
	
	if len(possible_solutions) == 0:
		case_return = case_num+': Volunteer cheated!'
	elif len(possible_solutions) == 1:
		case_return = case_num+': '+possible_solutions[0]
	else:
		case_return = case_num+': Bad magician!'
		
	out_file.write(case_return+'\n')
	
