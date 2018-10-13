fi = open("A-large.in")
fo = open("A-large.out", "w")

line = next(fi)
T = int(line)
for t in range(T):
	line = next(fi)
	[D,N] = [int(x) for x in line.rstrip().split(' ')]
	max_time = 0
	for i in range(N):
		line = next(fi)
		[K,S] = [int(x) for x in line.rstrip().split(' ')]
		max_time = max(max_time, (D-K)/S)
	speed = D / max_time

	fo.write("Case #" + str(t+1) + ": " + "{0:.6f}".format(speed) + "\n")

fi.close()
fo.close()
