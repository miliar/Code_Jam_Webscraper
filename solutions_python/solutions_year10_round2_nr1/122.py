import sys

in_file = open(sys.argv[1])
out_file = open("out.txt", 'w')

T = int(in_file.readline().strip())
for t in range(T):
	N, M = (int(x) for x in in_file.readline().strip().split())
	present = set()
	desired = set()
	for n in range(N):
		path = in_file.readline().strip()[1:].split("/")
		for i in range(len(path)):
			present.add(tuple(path[:i+1]))
	total = 0
	for m in range(M):
		path = in_file.readline().strip()[1:].split("/")
		for i in range(len(path)):
			needed = tuple(path[:i+1])
			if not needed in present:
				present.add(needed)
				total += 1
	output = "Case #%d: %d\n" % (t+1, total)
	print output,
	out_file.write(output)