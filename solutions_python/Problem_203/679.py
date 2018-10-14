def solve (f, s, cake):
	for i in range (f):
		for l in range (s):
			if cake[i][l] != '?':
				t = cake[i][l]

				for g in range (l+1, s ):
					if cake[i][g] == '?':
						cake[i][g] = t 
					else:
						break
				for k in range (l-1, -1, -1):
					if cake[i][k] == '?':
						cake[i][k] = t
					else:
						break

	for d in range (f):
		if cake[d][0] == "?":

			if d == 0:
				h = d
				while cake[h][0] == "?":
					h = h + 1

				for ii in range(s):
					cake[d][ii] = cake[h][ii] 
				
			else:

				for iii in range(s):
					cake[d][iii] = cake[d-1][iii]
					
	
	answer = ''
	for kkk in range (f):

		answer = answer + '\n' + ''.join(cake[kkk]) 
			

	return answer  















cake = []
case_num = 1
input_path = "../Downloads/A-large.in"
out = open('answer.txt', 'w')
with open(input_path) as f:
	lines = f.readlines()
	lines_head = int(lines[0].rstrip())
	lines_body = lines[1:]
	i = 0 
	g = 0 
	while i < lines_head:


		n = lines_body[g].rstrip()

		input_element_array = n.split()
		first_number = int(input_element_array[0])
		second_number = int(input_element_array[1])
		k = g + 1

		for z in range (first_number):
			g = k + z
			string_1 = lines_body[g].rstrip() # remove \n
			list_1 = list(string_1)
			cake.append(list_1)


		g = g + 1 

		
		i = i +1
		number = solve(first_number, second_number, cake)
		answer = "Case #"+ str(case_num) +": "

		out.write(answer + number +'\n')
		
		case_num = case_num +1
		cake = []


out.close()