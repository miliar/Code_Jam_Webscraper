def l_s(stalls, pos):
	l_s = 0
	
	for stall in reversed(stalls[:pos]):
		if not stall:
			l_s += 1
		else:
			break
	return l_s

def r_s(stalls, pos):
	r_s = 0
	
	for stall in stalls[pos + 1:]:
		if not stall:
			r_s += 1
		else:
			break
	return r_s
	

T = int(input())

for t in range(1, T + 1):
	N, K = [int(s) for s in input().split(" ")]
	
	stalls = [True] + [False] * N + [True]
	
	for k in range(1, K + 1):
		l_ss = [l_s(stalls, i) if not stalls[i] else -1 for i in range(1, len(stalls) - 1)]
		r_ss = [r_s(stalls, i) if not stalls[i] else -1  for i in range(1, len(stalls) - 1)]
		min_ls_rs = [min([l_ss[i], r_ss[i]]) for i in range(len(l_ss))]

		max_min = max(min_ls_rs)
		set_min = [i for i in range(len(min_ls_rs)) if min_ls_rs[i] == max_min]
		
		max_ls_rs = [max([l_ss[i], r_ss[i]]) if i in set_min else -1 for i in range(len(l_ss))]
		if (len(set_min) > 1):
		
			max_max = max(max_ls_rs)
			set_max = [i for i in range(len(max_ls_rs)) if max_ls_rs[i] == max_max]
			
			chosen_stall = set_max[0]
		else:
			chosen_stall = set_min[0]
			
		
		stalls[chosen_stall + 1] = True
		# print([(l_ss[i], r_ss[i]) for i in range(len(l_ss))])
		# print(min_ls_rs)
		# print(max_ls_rs)
		# print(set_min)
		# print(set_max)
		# print(chosen_stall)
	
	print("Case #{}: {} {}".format(t, max_ls_rs[chosen_stall], min_ls_rs[chosen_stall]))
	# print(min_ls_rs)
	# print(max_ls_rs)
	# print(set_min)
	# print(set_max)
	# print(chosen_stall)