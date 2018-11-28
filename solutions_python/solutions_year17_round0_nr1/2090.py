file_in = open("A-small-attempt0.in", "r")
file_out = open("A-small-attempt0.out", "w")

T = int(file_in.readline().rstrip())
for i in range(T):
	s = file_in.readline().rstrip().split()
	cakes = list(s[0])
	k = int(s[1])
	moves = 0
		
	if '-' not in cakes:
		file_out.write("Case #" + str(i+1) + ": " + str(moves) +"\n")
	
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
			file_out.write("Case #" + str(i+1) + ": " + str(moves) +"\n")
		else:
			file_out.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")

file_in.close()
file_out.close()