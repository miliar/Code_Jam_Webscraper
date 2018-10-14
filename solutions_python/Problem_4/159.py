fin = open("input.txt", "r")
fout = open("output.txt", "w")
for curCase in range(1, int(fin.readline()) + 1):
	size = int(fin.readline())
	v1 = map(int, fin.readline().split()[:size])
	v2 = map(int, fin.readline().split()[:size])
	v1.sort()
	v2.sort(lambda x, y: y - x)
	result = sum(map(lambda x,y: x*y, v1, v2))

	fout.write("Case #%i: %-d\n" % (curCase, result))
fin.close()
fout.close()