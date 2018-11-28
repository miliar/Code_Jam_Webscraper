#written by wegnahz

fin = open("Infinite House of Pancakes.in", "r")
fout = open("Infinite House of Pancakes.out", "w")

T = int(fin.readline())
for t in range(T):
	n = int(fin.readline())
	n_cakes = [int(s) for s in fin.readline().split(' ')]
	best = 1000000000
	for threshold in range(1, 1001):
		cnt = 0
		for n_cake in n_cakes:
			cnt += (n_cake-1) / threshold
		best = min(best, cnt+threshold)
	fout.write('Case #%d: %d\n' % (t+1, best))
