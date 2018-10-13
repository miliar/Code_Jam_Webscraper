number_of_test_case = int(raw_input())
t_counter = 1

while t_counter <= number_of_test_case:
	line = raw_input().strip().split()
	c = int(line[0])
	line_pointer = 1
	combine_dict = dict()
	while c > 0:
		s = line[line_pointer]
		if s[0] not in combine_dict:
			combine_dict[s[0]] = dict()
		if s[1] not in combine_dict:
			combine_dict[s[1]] = dict()
		combine_dict[s[0]][s[1]] = s[2]
		combine_dict[s[1]][s[0]] = s[2]
		line_pointer += 1
		c -= 1
	d = int(line[line_pointer])
	line_pointer += 1
	oppose_dict = dict()
	while d > 0:
		s = line[line_pointer]
		if s[0] not in oppose_dict:
			oppose_dict[s[0]] = set()
		if s[1] not in oppose_dict:
			oppose_dict[s[1]] = set()
		oppose_dict[s[0]].add(s[1])
		oppose_dict[s[1]].add(s[0])
		line_pointer += 1
		d -= 1
	ans = list()
	for s in line[line_pointer + 1]:
		if len(ans) > 0:
			if (ans[-1] in combine_dict) and (s in combine_dict[ans[-1]]):
				a = ans.pop()
				ans.append(combine_dict[a][s])
			elif (s in oppose_dict) and (len((oppose_dict[s] & set(ans))) > 0):
				ans = list()
			else:
				ans.append(s)
		else:
			ans.append(s)
	print 'Case #%d: [%s]' % (t_counter, ', '.join(ans),)
	t_counter += 1

