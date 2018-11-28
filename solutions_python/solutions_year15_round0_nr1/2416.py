def solve(shyness):
	clapping = 0
	ans = 0
	length = len(shyness)
	for i in range(length):
		need = i
		if need > clapping:
			ans += need - clapping
			clapping += (need - clapping) + int(shyness[i])
		else:
			clapping += int(shyness[i])
	return ans

f = open("/home/adijo/Downloads/A-large.in", "r")
op = open("StandingOvationRes.txt", "w")
t = int(f.readline())
for i in range(t):
	inp = f.next().split()
	shyness = inp[1]
	op.write("Case #%d" % (i + 1) +  ": " +  str(solve(shyness)) + "\n")
