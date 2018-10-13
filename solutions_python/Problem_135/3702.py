
def solve(magic_input, Test_case):

	if not magic_input[0]=='':
		first_row = magic_input[0]
		
		rowa = magic_input[int(first_row)].split()
		
		second_row = magic_input[5]
		
		rowb = magic_input[int(second_row)+5].split()
		

		coconut = 0
		answer=0

		for n in rowa:
			if n in rowb:
				coconut+=1
				answer=n

		if coconut == 0:
			print("Case #{0}: Volunteer cheated!".format(Test_case))

		if coconut == 1:
			print("Case #{0}: {1}".format(Test_case, answer))

		if coconut > 1:
			print("Case #{0}: Bad magician!".format(Test_case))

		solve(magic_input[10:], Test_case+1)

with open("/Users/JoeyOliver/Downloads/A-small-attempt1.in", encoding="utf-8") as inp:
	magic_input = inp.read().split('\n')

rounds = int(magic_input[0])

magic_input = magic_input[1:]

	
solve(magic_input, 1)

