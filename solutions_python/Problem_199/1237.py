T = int(input())
for t in range(T):
	[seq, size] = input().split()
	seq = list(seq)
	size = int(size)
	flips = 0
	ok = True
	n = len(seq)
	for i in range(n):
		if seq[i] == '+':
			continue
		else:
			if n-i < size:
				ok = False
				break
			else:
				flips = flips + 1
				for j in range(size):
					if seq[i+j] == '+':
						seq[i+j] = '-'
					else:
						seq[i+j] = '+'
	if ok:
		print("Case #{}: {}".format(t+1, flips))
	else:
		print("Case #{}: IMPOSSIBLE".format(t+1))
	
	
