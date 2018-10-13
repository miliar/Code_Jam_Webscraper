from heapq import heappush, heappop


def optimized(input_line):
	stalls, k = map(int, input_line.split())
	if stalls == k:
		return "0 0"
	h = []
	heappush(h, -stalls)

	for _ in range(k-1):
		c = heappop(h)

		if c < -2:
			heappush(h, (c+1)/2)
			heappush(h, (c+2)/2)
		else:
			if c == -2:
				heappush(h, -1)

	c = heappop(h)
	if c < -2:
		return str((0-c)/2)+" "+str((-1-c)/2)
	else:
		if c == -2:
			return "1 0"
		else:
			return "0 0"

if __name__ == "__main__":

	with open("output", 'w') as fout:
		f = open("C-small-1-attempt0.in")
		n = int(f.next())
		for i in range(n):
			line = f.next().strip()
			fout.write("Case #"+str(i+1)+": "+optimized(line.rstrip())+"\n")
		f.close()
