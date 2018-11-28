def check_ans(state):
	for i in range(len(state)):
		if (state[i] == "-"):
			return False

	return True
	
	

def solve(state, k):
	###Check for the consecutiveness
	state_arr = list(state)
	ret = 0

	for n in range(len(state_arr)):
		if (state_arr[n] == "-"):
			if (n + int(k) <= len(state_arr)):
				ret += 1
				for c in range(int(k)):
					if (state_arr[n + c] == "+"):
						state_arr[n + c] = "-"
					else:
						state_arr[n + c] = "+"

	final = "".join(state_arr)

	cfinal = check_ans(final)
	
	if (cfinal):
		return ret
	else:
		return "IMPOSSIBLE"



t = input()
#Impossible when the same state repeats
ans = []
for n in range(t):
	state, k = map(str, raw_input().split())

	check = check_ans(state)
	if (check):
		ans.append(0)
	else:
		ans.append(solve(state, k))
	

for i in range(1, t + 1):
	print "Case #{}: {}".format(i, ans[i - 1])
