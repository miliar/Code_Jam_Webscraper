vowels = ('a','e','i','o','u')

def n_value(s, val):
	count = 0
	temp = s.lower()
	while temp != "":
		consenants = 0
		for c in temp:
			if consenants >= val:
				count = count + 1
			elif not c in vowels:
				consenants += 1
				if consenants == val:
					count = count + 1
			else:
				consenants = 0
		temp = temp[1:]
	return count


def main():
	inp = open('input.txt', 'r')
	output = open('output.txt', 'w')
	cases = int(inp.readline())
	case = 1
	while cases > 0:
		case_input = inp.readline().split(' ')
		result = n_value(case_input[0], int(case_input[1]))
		output_string = 'Case #' + str(case) + ': ' + str(result) + '\n'
		output.write(output_string)
		cases = cases - 1
		case = case + 1

main()
