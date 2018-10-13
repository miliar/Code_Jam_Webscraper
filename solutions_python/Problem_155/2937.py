fr = open("input.txt","r")
fw = open("output.txt","w")
tcase = int(fr.readline())

for tc in range(1, tcase+1):
	

	N,S = map(str,fr.readline().split())
	N = int(N)
	hadirin = 0
	tambah = 0
	for i in range(0,N+1):
		j = int(S[i])
		if j:
			if hadirin < i:
				tambah += (i-hadirin)
				hadirin += j + (i-hadirin)
			else:
				hadirin += j;
			
	fw.write("Case #%d: %d\n" % (tc,tambah))

fr.close()
fw.close()
