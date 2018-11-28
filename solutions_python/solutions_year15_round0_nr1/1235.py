def solve(shyness):
	total = shyness[0]
	invited = 0
	for i in range(1, len(shyness)):
		if shyness[i] != 0 and total < i: #check if need to invite
			extra = i - total
			invited += extra
			total += extra
		total += shyness[i]
	return invited




if __name__ == '__main__':
	in_file = open('A-large.in', 'r')
	out_file = open('out.txt', 'w')

	test_cases = int(in_file.readline())
	for test_case in range(test_cases):
		s_max, levels = in_file.readline().split()
		shyness = [int(x) for x in levels]
		out_file.write("Case #%d: %d\n"%(test_case+1, solve(shyness)))
	out_file.close()
		