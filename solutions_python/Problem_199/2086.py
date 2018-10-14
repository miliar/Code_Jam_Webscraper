def flipping(seq, k):
	l_seq = len(seq)
	i = 0
	t_flip = 0
	while i <= l_seq - k:
		if seq[i] == "-":
			t_flip = t_flip + 1
			addseg = ""
			for j in range(k):
				if seq[i+j] == "-":
					addseg = addseg + "+"
				else:
					addseg = addseg + "-"
			seq = seq[:i] + addseg + seq[i+k:]
		i = i + 1
	for ele in seq[-k:]:
		if ele == "-":
			return "IMPOSSIBLE"
	return t_flip


t = int(input())
for i in range(1, t + 1):
	n, m = [s for s in input().split(" ")]
	m = int(m)
	result = flipping(n, m)
	print("Case #%d: %s" %(i, result))