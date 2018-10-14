#written by wegnahz

fin = open("Standing Ovation.in", "r")
fout = open("Standing Ovation.out", "w")
T = int(fin.readline())
for t in range(T):
	tokens = fin.readline().split(' ')
	s_max = int(tokens[0])
	n_friends = cur_sum = 0	
	for shyness in range(s_max+1):
		n_cur = int(tokens[1][shyness])
		if cur_sum + n_friends < shyness:
			n_friends = shyness - cur_sum
		cur_sum += n_cur
	fout.write('Case #%d: %d\n' % (t+1, n_friends))
