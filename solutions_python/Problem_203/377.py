
t = int(input())
for tc in range(1, t + 1):
	R, C = [int(x) for x in raw_input().split()]
	M = [list(raw_input()) for x in range(R)]
	index_of_copyable_row = ''
	has_at_least_one_empty_row = False
	for i in range(R):
		isEmpty = True
		current_char = ''
		for j in range(C):
			if (M[i][j] != '?'):
				isEmpty = False;
				current_char = M[i][j]
				break
		if not isEmpty:
			for j in range(C):
				if (M[i][j] == '?'):
					M[i][j] = current_char
				else:
					current_char = M[i][j]
		else:
			has_at_least_one_empty_row = True
	if has_at_least_one_empty_row:
		for i in range(R):
			if M[i][0] != '?':
				index_of_copyable_row = i
				break
		for i in range(R):
			if M[i][0] == '?':
				M[i] = M[index_of_copyable_row]
			else:
				index_of_copyable_row = i
	print("Case #{}:\n{}".format(tc,"\n".join(["".join(x) for x in M])))
  