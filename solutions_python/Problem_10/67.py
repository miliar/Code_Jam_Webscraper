fin = open("input.txt", "r")
fout = open("output.txt", "w")
for curCase in range(1, int(fin.readline()) + 1):
	(P, K, L) = map(int, fin.readline().split())
	letters = map(int, fin.readline().split()[:L])
	if P * K < L:
		result = "Impossible"
	else:
		letters.sort(lambda x,y: y - x)
		result = sum([letters[i]*(i//K + 1) for i in range(L)])
	fout.write("Case #%i: %d\n" % (curCase, result))
fin.close()
fout.close()