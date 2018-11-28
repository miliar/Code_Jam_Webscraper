def do_case():
	s, k = input().split()
	k = int(k)
	inp = [i == "+" for i in s]
	# make all true!
	flips = 0
	for left in range(0, len(inp) - k + 1):
		if not inp[left]:
			flips += 1
			for offset in range(k):
				inp[left + offset] = not inp[left + offset]
	if all(inp):
		return flips
	else:
		return "IMPOSSIBLE"

t = int(input())

for case in range(1, t+1):
	print("Case #{}: {}".format(case, do_case()))