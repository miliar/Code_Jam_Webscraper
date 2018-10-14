T = int(input())
for t in range(T):
	seq = [int(x) for x in list(input())]
	n = len(seq)
	flip = len(seq)
	for i in range(len(seq)-1, 0, -1):
		if seq[i] >= seq[i - 1]:
			continue
		else:
			seq[i - 1] = seq[i - 1] - 1
			flip = i
	
	for i in range(flip, len(seq)):
		seq[i] = 9
	
	pos = 0
	for c in seq:
		if c == 0:
			pos = pos+1
		else:
			break
	seq = seq[pos:]
	seq = [str(c) for c in seq]
	seq = ''.join(seq)
	
	print("Case #{}: {}".format(t+1, seq))

	
	
