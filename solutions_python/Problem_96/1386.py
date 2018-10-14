import os

inp = open("input.txt", "r");
src = inp.readlines();
out = open("output.txt", "w");
for i in range(1, len(src)):
	ninp = src[i].split(' ')
	n = int(ninp[0])
	t = int(ninp[1])
	p = int(ninp[2])
	lst = map(lambda x: int(x), ninp[3:])
	(t1, t2, t3) = reduce(lambda (z1, z2, z3), x: (z1 + int(x < 3*p-4), z2 + int(x >= 3*p-4 and x < 3*p-2 and x >= p), z3 + int(x >= 3*p-2)), lst, (0,0,0) )
	ans = t3
	if t2 > t:
		t2 = t
	ans = ans + t2
	out.write("Case #" + str(i) + ": " + str(ans) + "\n")
