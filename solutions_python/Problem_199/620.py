
#inp = open("input.in", "r")
#inp = open("A-small-attempt0.in", "r")
inp = open("A-large.in", "r")

#outp = open("output.out", "w")
#outp = open("A-small-attempt0.out", "w")
outp = open("A-large.out", "w")


T = int(inp.readline().rstrip())

for i in range(T):
	s = inp.readline().rstrip().split()
	cakes = list(s[0])
	k = int(s[1])
	moves = 0
		
	if '-' not in cakes:
		outp.write("Case #" + str(i+1) + ": " + str(moves) +"\n")
	
	else:			
	
		for c in range(len(cakes)-k+1):
			if cakes[c]=='-':
				moves += 1
				flip=0
				while flip<k:
					if cakes[c+flip]=='+':
						 cakes[c+flip] = '-'
					elif cakes[c+flip]=='-':
						cakes[c+flip] = '+'
					flip += 1

		if '-' not in cakes:
			outp.write("Case #" + str(i+1) + ": " + str(moves) +"\n")
		else:
			outp.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")


inp.close()
outp.close()