import math
import Queue

def occupyStall(n, p):
	# if n == 1:
	# 	return n, p + 1, n, n - 1
	if n % 2 == 0:
		n = n / 2
		return n, p + 1, n, n - 1
	else:
		n = n - 1
		return n, p + 1, n / 2, n / 2

f_in = open("C-small-1-attempt1.in", "r")
f_out = open("bathroom_stalls_output", "w")
numTests = int(f_in.readline())
for x in range(numTests):
	data = str(f_in.readline()).split(' ')
	n = int(data[0])
	k = int(data[1])
	p = 1
	y = 0
	z = 0
	queue = Queue.PriorityQueue()
	while p < k + 1:
		n, p, y, z = occupyStall(n, p)
		queue.put((-y, y))
		queue.put((-z, z))
		n = queue.get(0)[1]
	f_out.write("Case #" + str(x + 1) + ": " + str(y) + " " + str(z))
	if x < numTests - 1:
		f_out.write("\n")