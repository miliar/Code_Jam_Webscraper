T = int(raw_input())

for t in range(T):
	(N,K) = map(int,raw_input().split(" "))
	spaces = [N]
	for k in range(K-1):
		gap = spaces.pop()
		spaces.append((gap-1)/2)
		spaces.append(gap-(gap-1)/2-1)
		spaces.sort()
	gap = spaces.pop()
	print "Case #{0}: {1} {2}".format(t+1,gap-(gap-1)/2-1,(gap-1)/2)