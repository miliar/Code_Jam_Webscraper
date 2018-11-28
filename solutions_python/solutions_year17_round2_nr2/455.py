import sys

def solve(N, R, O, Y, G, B, V):
	stall = ""
	colors = ['R', 'Y', 'B']
	nums = [R, Y, B]
	lastIndex = -1
	firstIndex = -1

	possible = True
	for i in xrange(N):
		index = -1
		m = -1
		for j in xrange(len(nums)):
			num = nums[j]
			if num > 0:
				if num == m and j != lastIndex:
					if j == firstIndex:
						index = j
				elif num > m and j != lastIndex:
					index = j
					m = num

		if m == -1:
			possible = False
			break

		if firstIndex == -1:
			firstIndex = index

		nums[index] = nums[index] - 1
		stall += colors[index]
		lastIndex = index

	if stall[0] == stall[-1]:
		possible = False

	if possible:
		return stall
	else:
		return "IMPOSSIBLE"

f = open("B-small-attempt2.in")
rl = lambda: f.readline().strip()

output = open("output.txt", 'w')

T = int(rl())
for i in xrange(T):
	l = rl().split()
	N = int(l[0])
	R = int(l[1])
	O = int(l[2])
	Y = int(l[3])
	G = int(l[4])
	B = int(l[5])
	V = int(l[6])

	out = "Case #%d: %s\n" % (i + 1, solve(N, R, O, Y, G, B, V))
	print out
	output.write(out)
