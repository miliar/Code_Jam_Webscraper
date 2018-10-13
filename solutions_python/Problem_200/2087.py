
T = int(input())

for i in range(1, T + 1):
	N = input()
	
	
	all_correct = False
	while not all_correct:
	
		result = ""
		correct = True
		for digit in range(len(N) - 1):
			if not correct:
				result += '9'
			
			else:
				correct = N[digit] <= N[digit + 1]
				if correct:
					result += N[digit]
				else:
					result += str(int(N[digit]) - 1)
				
				
		if correct:
			result += N[-1]
		else:
			result += '9'
			
		N = result
		all_correct = True
		for digit in range(len(N) - 1):
			all_correct &= N[digit] <= N[digit + 1]
		

	print("Case #{}: {}".format(i, int(N)))