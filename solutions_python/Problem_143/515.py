#MAM, Google Code Jam - Round 1B, Problem B

infile = open("B-small-attempt0.in", "r")
outfile = open("output.txt", "w")

numtests = int(infile.readline())

for T in range(numtests):

	#Input

	(A, B, K) = map(int, infile.readline().split(' '))

	#Calculations

	if B > A:
		A, B = B, A

	kbins = range(K)
	abins = range(A)
	bbins = range(B)

	counter = 0
	for eacha in abins:
		for eachb in bbins:
			if eacha&eachb in kbins:
				counter+=1

	#Output
	outfile.write("Case #"+str(T+1)+": ")
	outfile.write(str(counter))
	outfile.write("\n")