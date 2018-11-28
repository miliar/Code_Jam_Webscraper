cases = int(raw_input())



def check_number(number):
	for i in xrange(len(number)-1):
		if number[i] < number[i+1]:
			return False
	return True


def reduce_number(number):
	for i in xrange(len(number)):
		number[i] -= 1
		if number[i] != 0:
			break
		else:
			number[i] = 9
	else:
		if number[-1] == 9:
			number.pop()


for i in xrange(cases):
	number = map(int, list(raw_input()))
	number.reverse()
	solution = []

	while not check_number(number):
		number.pop(0)
		solution.append(9)
		reduce_number(number)

	solution.extend(number)
	solution.reverse()
	solution = map(str, solution)
	print "Case #{0}: {1}".format(i+1, ''.join(solution))