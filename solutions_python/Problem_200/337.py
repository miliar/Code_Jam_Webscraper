fin = open('B-large.in', 'r')
fout = open('B-large.out','w')






numlines = int(fin.readline().rstrip())

for line in range(numlines):
	vals = str(fin.readline().rstrip())
	# (N,) = tuple([c for c in vals.split(" ")])
	
	N = [int(c) for c in vals]
	
	for i in range(len(N)-1):
		if N[i] > N[i+1]:
			while N[i] == N[i-1] and i > 0:
				i = i - 1
			N[i] = N[i] - 1
			for j in range(i+1,len(N)):
				N[j] = 9
			break
	
	i = 0
	while N[i] == 0:
		N[i] = ""
	result = "".join([str(i) for i in N])

	outstr = "Case #" + str(line+1) + ": " + str(result) + "\n"
	# print result.rstrip()
	fout.write(outstr)




