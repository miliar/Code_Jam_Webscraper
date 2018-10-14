def standing_ovation(filename):
	with open(filename, "r") as input_f:
		no_of_test_cases = int(input_f.readline())
		x = 0
		j = 0
		while x < no_of_test_cases:
			case = input_f.readline().replace('\n','').split(' ')
			if len(case) < 2:
				no_of_test_cases = case[0]
				case = input_f.readline().replace('\n','').split(' ')
				j = 0
				if case[0] == '': return
			friends = 0
			for (i,number) in enumerate(case[1]):
				if int(number) == 0:
					pass
				else:
					total = sum(map(int,case[1][0:i]))
					if total < i and ((i-total) > friends):
						friends = i-total
			mode = 'a'			
			with open('A-large.out',mode) as output_f:
				output_f.write('Case #%d: %d\n' %(j+1,friends))
			j+=1
standing_ovation("A-large.in")