name = "A-large"
i = open(name + ".in", 'r')
o = open(name + ".out", 'w')

def calc(s):
	needed = 0;
	extra = 0;
	for c in s:
		n = int(c)
		extra += n-1
		if extra < 0:
			needed -= extra
			extra = 0
	return needed


lines = i.readlines()
for t in range(1, int(lines[0])+1):
	n, s = lines[t].split()
	result = calc(s)
	o.write("Case #{}: {}\n".format(t, result))