def current_state(n):
	state = {}
	for i in range(n):
		state[i] = (i, n-1-i)
	return state


def pick_stall(cr_state):
	max_of_min_stalls = []
	max_min = float("-inf")

	for i in range(len(cr_state)):
		if cr_state[i]!="O":
			if min(cr_state[i]) > max_min:
				max_of_min_stalls.clear()
				max_of_min_stalls.append(i)
				max_min = min(cr_state[i])
			elif min(cr_state[i]) == max_min:
				max_of_min_stalls.append(i)

	if len(max_of_min_stalls)>1:
		max_max = float("-inf")
		max_of_max_stalls = []
		for i in max_of_min_stalls:
			if max(cr_state[i]) > max_max:
				max_of_max_stalls.clear()
				max_of_max_stalls.append(i)
				max_max = max(cr_state[i])
			elif max(cr_state[i]) == max_max:
				max_of_max_stalls.append(i)

		if len(max_of_max_stalls) > 1:
			return sorted(max_of_max_stalls)[0]
		else:
			return max_of_max_stalls[0]
	return max_of_min_stalls[0]


def update_state(cr_state, idx):
	less = (idx-1)
	while less>=0 and cr_state[less]!="O":
		new = cr_state[less][0], abs(cr_state[idx][0]-cr_state[less][0]-1)
		cr_state[less] = new
		less-=1

	more = idx+1
	while more<len(cr_state) and cr_state[more]!="O":
		new = abs(cr_state[more][0]-cr_state[idx][0]-1), cr_state[more][1]
		cr_state[more] = new
		more+=1
	cr_state[idx] = "O"

	return cr_state


def main(n, k):
	state = current_state(n)
	for i in range(k):
		pick = pick_stall(state)
		ans = max(state[pick]), min(state[pick])
		new_state = update_state(state, pick)
	return ans



T = int(input())
for T0 in range(T):
	N, K = input().split(" ")
	if int(N)==int(K):
		ans = 0,0
	else:
		ans = main(int(N), int(K))

	print("Case #{}: {} {}".format(T0+1, ans[0], ans[1]))

