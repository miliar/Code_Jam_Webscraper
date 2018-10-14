def solution(s, k, iteration):
	p = []
	for i in s:
		if i == "+":
			p.append(True)
		else:
			p.append(False)

	counter = 0

	for i in range(len(p) - k + 1):
		if not p[i]:
			counter += 1
			for j in range(k):
				p[i+j] = not p[i+j]

	for i in range(len(p) - 1, len(p) - 1 - k , -1):
		if not p[i]:
			return "Case #" + str(iteration) + ": IMPOSSIBLE"

	return "Case #" + str(iteration) + ": " + str(counter)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]
  print solution(n, int(m), i)

  #print "Case #{}: {} {}".format(i, n + m, n * m)











