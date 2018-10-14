T = int(raw_input().strip())
col = {}
col['R'] = ['Y', 'G', 'B']
col['O'] = ['B']
col['Y'] = ['R', 'B', 'V']
col['G'] = ['R']
col['B'] = ['R', 'Y', 'O']
col['V'] = ['Y']

colours = ['R', 'O', 'Y', 'G', 'B', 'V']
high_prio = ['O', 'G', 'V']
low_prio = ['R', 'G', 'B']

for t in range(1, T+1):
	C = map(int, raw_input().strip().split())
	N = C[0]
	S = []
	have = {}
	have['R'] = C[1]
	have['O'] = C[2]
	have['Y'] = C[3]
	have['G'] = C[4]
	have['B'] = C[5]
	have['V'] = C[6]
	for c in colours:
		if have[c]:
			S.append(c)
			have[c] -= 1
			break

	# try greedy
	current_ind = 0
	while current_ind < N:
		poss = col[S[current_ind]]
		max_u = 0
		max_col = ''
		for p in poss:
			if p in high_prio and have[p] > max_u:
				max_u = have[p]
				max_col = p
		if max_u == 0:
			for p in poss: 
				if have[p] > max_u:			
					max_u = have[p]
					max_col = p
		if max_u == 0:
			break		
		S.append(max_col)
		have[max_col] -= 1
		current_ind += 1
	
	if len(S) == N and (N == 1 or S[0] in col[S[-1]]):
		ans = ''.join(S)
	else:
		ans = 'IMPOSSIBLE'

	print 'Case #{0}: {1}'.format(t, ans)



