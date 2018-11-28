fi = open("input.txt", "r")
fo = open("output.txt", "r+")

cases = int(fi.readline())

for case in range(cases):
	counter = 0
	l = map(int, fi.readline().rstrip().split())
	a = l[0]
	b = l[1]
	c = l[2]
	for i in range(a):
		for j in range(b):
			if (i & j < c):
				counter += 1
	fo.write("Case #" + str(case + 1) + ": " + str(counter) + "\n")