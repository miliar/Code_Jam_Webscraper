T = input()
for t in range(T):
	line = raw_input().split()
	pancake_state = line[0]
	K = int(line[1])
	
	pancake_state = pancake_state.strip('+')
	flip_cnt = 0
	while K <= len(pancake_state):
		new_leading = ''
		for i in range(K):
			if pancake_state[i] == '+':
				new_leading = new_leading + '-'
			else:
				new_leading = new_leading + '+'
		pancake_state = new_leading + pancake_state[K:]
		pancake_state = pancake_state.strip('+')
		flip_cnt = flip_cnt + 1
	if len(pancake_state) == 0:
		print 'Case #'+str(t+1)+': '+str(flip_cnt)
	else:
		print 'Case #'+str(t+1)+': IMPOSSIBLE'
