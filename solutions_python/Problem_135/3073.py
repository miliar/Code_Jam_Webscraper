import sets
#fin_name = "p1_input.in"
fin_name = "A-small-attempt5.in"
fout_name = "p1.out"
with open(fin_name) as fin:
    content = fin.readlines()

fout = open(fout_name, 'r+')

num_cases = content[0]

case_index = 0
lines_per_case = 10
for case_index in range(0,int(float(num_cases))): 
	#print (case_index * lines_per_case)
	first_guess = int(float(content[case_index * lines_per_case + 1])) 
	second_guess = int(float(content[case_index * lines_per_case + 5 + 1]))
	options_first_guess = content[case_index * lines_per_case + first_guess + 1]
	options_second_guess = content[case_index * lines_per_case + 5 + second_guess + 1]
	first_row = options_first_guess.split()
	second_row = options_second_guess.split()
	
	s1 = sets.Set(first_row)
	s2 = sets.Set(second_row)
	intersection = list(s1.intersection(s2))

	# one unique solution
	if len(intersection) == 1:
		fout.write("Case #"+str(case_index+1)+": " + str(intersection[0])+"\n")
	elif len(intersection) == 0:
		fout.write("Case #"+str(case_index+1)+": Volunteer cheated!\n")
	elif len(intersection) > 1:
		fout.write("Case #"+str(case_index+1)+": Bad magician!\n")

	
	