infile = open("B-large.in", "r")
lines = infile.readlines()
outfile = open("out.out", "w")
tc = int(lines[0])


for t in range(tc):
	n = lines[t+1].strip()	
	i = len(n) - 1

	while(i >= 1):
		if n[i] < n[i-1]:	
			nines = ""
			for x in range(i+1, len(n)):
				nines = nines + "9"		
			n = n[0:i-1] + str(int(n[i-1]) - 1) + "9" + nines
		i -= 1

	outfile.write("Case #" + str(t+1) + ": " + str(n.lstrip('0')) + "\n")
			