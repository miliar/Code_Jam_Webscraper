def flip_nums(str_pat, flips, nums=0):
	if "-" not in str_pat:
		return nums

	try:
		minus_idx = str_pat.index("-")
		if len(str_pat)-minus_idx>=flips:
			start = minus_idx
		else:
			start = minus_idx-(flips-(len(str_pat)-minus_idx))

		for i in range(start, start+flips):
			if str_pat[i]=="-":
				str_pat[i]="+"
			else:
				str_pat[i]="-"
		return flip_nums(str_pat, flips, nums+1)
	except Exception:
		return "IMPOSSIBLE"



T = int(input())
for T0 in range(T):
	
	S, K = input().split(" ")
	ans = flip_nums(list(S), int(K))

	print("Case #{}: {}".format(T0+1, ans))

