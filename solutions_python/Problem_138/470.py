def war(f, s):
	for fb in f:
		for si in range(len(s)):
			sn = s[si]
			if fb < sn:
				del s[si]
				break
	return len(s)


fin=open("D-large.in","r")
fout=open("output.txt","w")

cases=int(fin.readline())

for case in xrange(cases):
	n = fin.readline()
	nBlocks = map(lambda x: float(x), fin.readline().rstrip().split(" "))
	kBlocks = map(lambda x: float(x), fin.readline().rstrip().split(" "))
	blockCount = len(nBlocks)

	nBlocks.sort()
	kBlocks.sort()

	dwRes = blockCount - war(kBlocks, nBlocks[:])
	wRes = war(nBlocks, kBlocks)	
	
	fout.write("Case #{0}: {1} {2}\n".format(str(case + 1) , dwRes, wRes))
	
fin.close()
fout.close()