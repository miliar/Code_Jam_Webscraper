def do_case():
	inp = list(map(int, input()))
	n = len(inp)
	done = False
	while not done:
		done = True
		for left in range(n-1):
			right = left + 1
			if inp[left] > inp[right]:
				done = False
				# subtract 1 from inp[left]
				# wait what if it's 0?
				# it can't be 0, lol.
				inp[left] -= 1
				# set 9s to the right
				for i in range(right, n):
					inp[i] = 9
	return "".join(map(str, inp)).lstrip("0")
	

t = int(input())

for case in range(1, t+1):
	print("Case #{}: {}".format(case, do_case()))