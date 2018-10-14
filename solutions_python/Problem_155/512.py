T = int(raw_input())
cas = 0
f = open("out.txt", "w");
while T > 0:
	T -= 1
	n, s = raw_input().split()
	last = 0
	res = 0
	for i, c in enumerate(s):
		if i > last:
			res += i - last
			last += i - last
		last += int(c)
	cas += 1
	f.write("Case #" + str(cas) + ": " + str(res) + '\n')