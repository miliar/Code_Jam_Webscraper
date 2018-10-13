
import Code_Ninja_Contest_Utilities as cncu 

def solver(case):
	answer = case[0][0]
	answer2 = case[5][0]
	grid1 = case[1:5] 
	grid2 = case[6:10] 
	row1 = grid1[answer-1]
	row2 = grid2[answer2-1]
	
	possible_numbers = filter(lambda x: x in row1, row2)
	print possible_numbers
	if len(possible_numbers) == 1: 
		return possible_numbers[0]
	if len(possible_numbers) == 0:
		return "Volunteer cheated!" 
	if len(possible_numbers) >1: 
		return "Bad magician!"

num_cases, cases = cncu.read_infile("in.txt", True)
cases = cncu.grouplist(cases, 10)
cases=[[map(int,n) for n in y] for y in cases] 

store_results = [] 
for varry in cases: store_results.append(solver(varry))

cncu.write_outfile(store_results, "outy.txt")
		

