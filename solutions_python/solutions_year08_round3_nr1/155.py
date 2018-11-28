def sort1(x, y):
	return cmp(y, x)

def doTest(fin, fout, testIdx):
	P, K, L = fin.readline().split()
	#print P, K, L
	freq_list_s = fin.readline().split()
	freq_list = []
	for s in freq_list_s:
		n = int(s)
		freq_list.append(n)
	freq_list.sort(sort1)
	#print freq_list
	keyPresses = 0
	x = 0
	col = 1
	k = int(K)
	for i in range(int(L)):
		keyPresses = keyPresses + freq_list[i] * col
		x = x + 1
		if x == k:
			x = 0
			col = col + 1
	fout.write("Case #%d: %d\n" % (testIdx, keyPresses))

fin = open("A-large.in", "r")
fout = open("A-large.out", "w")
numTests = int(fin.readline())
for i in range(numTests):
	doTest(fin, fout, i+1)
fin.close()
fout.close()
