def read(path):
	file_in = open(path, 'r')

	case = 0
	start = 0
	for line in file_in:
		if case == 0:
			case +=1
		else:
			if start == 0:
				start += 1
			else:
				start = 0
				temp = line.split()
				lst = [int(i) for i in temp]
				result = solve(lst)
				sol = ""
				for i in range(len(result)):
					if i == len(result) -1:
						sol += str(result[i])
					else:
						sol += str(result[i]) + " "
				string = "Case #" + str(case) + ": " + sol

				print string
				case += 1
def solve(lst):
	res1 = 0
	i = 0
	# while i < len(lst):
	for i in range(len(lst)):
		if i < len(lst)-1:
			if lst[i+1] > lst[i]:
				pass
			else:
				res1 += lst[i] - lst[i+1]
		i += 1

	res2 = 0
	decrease = False
	max_rate = 0
	for i in range(len(lst)):
		if i < len(lst)-1:
			if lst[i] - lst[i+1] > max_rate:
				max_rate = lst[i] - lst[i+1]
	
	for i in range(len(lst)):
	# i = 0
	# while i < len(lst):
		if i < len(lst)-1:
			if lst[i+1] < lst[i]:
				decrease = True
			if lst[i] > max_rate:
				res2 += max_rate
			else:			
				res2 += lst[i]
		i+=1

	if not decrease:
		return res1, 0
	else:
		return res1, res2

# print solve([10, 5, 15, 5])
# print solve([81, 81])
# print solve([81, 81, 81, 81, 81, 81, 81, 0])
# print solve([23, 90, 40, 0, 100, 9])

# read("A_test_in.txt")
# read("A-small-attempt1.in")
read("A-large.in")