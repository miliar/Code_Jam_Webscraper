import sys

if len(sys.argv) != 3 :
	print "Usage: python TT.py inputfile outputfile"
	sys.exit(1)

infile = sys.argv[1]
inp = open(infile)
outfile = sys.argv[2]
outp = open(outfile, "w")

def split_into_int(input, delim) :
	a, b = input.strip().split(delim)
	if a[0] == '0' :
		a = a[1]
	if b[0] == '0' :
		b = b[1]
	a = int(a)
	b = int(b)
	return (a, b)

def get_num_departures(AtoB, BtoA) :
	A = []
	B = []
	for e in AtoB :
		A.append(e)
	for e in BtoA :
		B.append(e)
	
	numA = len(A)
	A.sort()
	B.sort(cmp=lambda x, y: x[1]-y[1])
	for (depA, arrA) in A :
		for (depB, arrB) in B :
			if arrB <= depA :
				B.remove((depB, arrB))
				numA -= 1
				break
	B = []
	for e in BtoA :
		B.append(e)	
	A.sort(cmp=lambda x, y: x[1]-y[1])
	B.sort()
	numB = len(B)
	for (depB, arrB) in B :
		for (depA, arrA) in A :
			if arrA <= depB :
				A.remove((depA, arrA))
				numB -= 1
				break
	return (numA, numB)

def get_timelist(num_lines, T, input=inp) :
	timelist = []
	for j in range(0, num_lines) :
		dep, arr = input.readline().split()
		(hour, min) = split_into_int(dep, ':')
		dep = 60 * hour + min
		(hour, min) = split_into_int(arr, ':')
		arr = 60 * hour + min + T
		timelist.append((dep, arr))
	return timelist

num_cases = int(inp.readline())
i = 1
while i <= num_cases:
	turn = int(inp.readline())
	(AtoB, BtoA) = split_into_int(inp.readline(), ' ')
	AtoBlist = get_timelist(AtoB, turn)
	BtoAlist = get_timelist(BtoA, turn)
	(numA, numB) = get_num_departures(AtoBlist, BtoAlist)
	line = "Case #" + str(i) + ": " + str(numA) + " " + str(numB)
	outp.write(line + '\n')
	i += 1

inp.close()
outp.close()
