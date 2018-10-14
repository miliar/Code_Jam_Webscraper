import math
from itertools import islice

def solve(question):
	length = int(math.floor(math.log(max(question),2))) + 1
	#print length
	parity = []
	for i in range(0,length):
		parity.append(0)
	for numbers in question:
		bn = bin(numbers)[2:]
		fullbn = ""
		for i in range(0, length-len(bn)):
			fullbn += '0'
		fullbn = fullbn + bn
		#print str(numbers) + ": " + str(fullbn)
		for i in range(0,length):
			if(int(fullbn[i]) > 0):
				if(parity[i]):
					parity[i] = 0
				else:
					parity[i] = 1
	#print parity
	#print "\n\n\n\n\n\n\n\n\n"
	if(max(parity) == 0):
		return sum(question) - min(question)
	else:
		return "NO"
	

def grabproblem(infile,outfile):
	f = open(infile)
        g = open(outfile,'a')

	i = 0
	j = 0
	with open(infile) as myfile:
        	cases=list(islice(myfile,1))
        	n = int(cases[0])
        for i in range(1,2*n+1):
        	with open(infile) as myfile:
			case = list(islice(myfile,i,i+1))
			if(i%2 != 0):
				m = int(case[0])
			else:
				j = j + 1
				thiscase = case[0].split(" ")
				print thiscase
				for i in range (0,m-1):
					thiscase[i] = int(thiscase[i])
				thiscase[m-1] = int(thiscase[m-1][0:len(thiscase[m-1])])
				print thiscase
				g.write("Case #" + str(j) + ":" + " " + str(solve(thiscase)) + "\n")
				#"Case #" + str(j) + ":" + " " + str(solve(thiscase,j)) + "\n"
				#solve(thiscase,j)

grabproblem("in.txt","out.txt")
