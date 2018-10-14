import math

def findLength ( i ):
	div = 1
	len = 0
	while div <= 10000000:
		if i/div == 0:
			return len
		len += 1
		div *= 10

			 

def solve (A, B):
	len = findLength ( A )
	i = A
	num = 0
	while i <  B:
		store=[]
		k = 1
		while k < len:
			rn = i%pow(10,k)*pow(10,len-k)+i/pow(10,k)
			if rn <= B and rn > i and store.count(rn) == 0:
				num += 1
				store.append(rn)
			k += 1
		i += 1
	return num	

		

def solveProblem(lnum,line):
    i = 0
    j = 0
    A = 0
    B = 0
    while i < 2:
        num=''
	while line[j] != ' ' and line[j] != '\n':
		num += line[j]
		j += 1
	if i == 0:
		A = int(num)
	else:
		B = int(num)
	i += 1
	j += 1
    print "Case #{num}: {result}".format(num=lnum,result=solve(A,B))

inputFile = open ( 'A-small.in', 'r')

lnum = 0
for line in inputFile:
    if lnum == 0:
	numTestCases = int(line)
    elif lnum > numTestCases:
	break
    else:
	if lnum == numTestCases:
		line += '\n'
	solveProblem(lnum,line)
    lnum += 1

