fi = open("B-large.in")
fo = open("B-large.out", "w")

line = next(fi)
T = int(line)
for t in range(T):
	line = next(fi)
	N = line.rstrip()
	tidy = ""
	if len(N)==1:
		tidy = N
	else:
		for i in range(1,len(N)):
			if int(N[i-1]) > int(N[i]):
				j = i-1
				for k in range(i,0,-1):
					j = k-1
					if j==0 or int(N[j-1]) < int(N[j]):
						break
				tidy += N[:j]
				n = int(N[j])-1
				if j>0 or n>0:
					tidy += str(n)
				for k in range(j+1, len(N)):
					tidy += "9"
				break
		if tidy=="":
			tidy = N

	fo.write("Case #" + str(t+1) + ": " + tidy + "\n")

fi.close()
fo.close()
