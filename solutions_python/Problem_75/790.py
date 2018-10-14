import math
from itertools import islice


def solve(question):
	combines = int(question[0])
	conflicts = int(question[combines+1])
	sequencelen = int(question[combines+conflicts+2])
	seq = question[combines+conflicts+3]
	sequence = []
	for i in range(0,len(seq)):
		sequence.append(seq[i])
	combine = {}
	for i in range(0,combines):
		combine[question[i+1][:2]] = question[i+1][2:]
	conflict = []
	for i in range(0,conflicts):
		conflict.append(question[combines+i+2])
	j = 0 
	parsecount = 0
	flag = 0
	for i in range(0,sequencelen):
		if(parsecount == sequencelen):
			break
		if(j > 0):
			print "J: " + str(j)
			#print sequence[j-1]
			lasttwoA = sequence[j-1] + sequence[j]
			lasttwoB = sequence[j] + sequence[j-1]
			#print sequence
			if(getcomb(lasttwoA,combine)):
				del sequence[j]
				sequence[j-1] = getcomb(lasttwoA,combine)
				parsecount = parsecount + 1
				continue
			if(getcomb(lasttwoB,combine)):
				del sequence[j]
				sequence[j-1] = getcomb(lasttwoB,combine)
				parsecount = parsecount + 1
				continue
			for r in range(0,j):
				print "r = " + str(r)
				print "---" 
				print "j = " + str(j)
				if(sequence[r]+sequence[j] in conflict or sequence[j]+sequence[r] in conflict):
					#print conflict
					del sequence[0:j+1]
					j = 0
					parsecount = parsecount + 1					
					flag = 1
					break
			if(flag):
				flag = 0
				continue
			j = j+1
			parsecount = parsecount + 1
		else:
			j = j+1
			parsecount = parsecount + 1
	answer = "["
	if len(sequence) > 0:
		for i in range(0,len(sequence)-1):
			answer += sequence[i] + ", "
		answer += sequence[len(sequence)-1] 
	answer += "]"
	print answer
	print '----------'
	return answer

def getcomb(element,combarray):
	if(element in combarray):
		return combarray[element]

def grabproblem(infile,outfile):
	f = open(infile)
        g = open(outfile,'a')

	i = 0
	j = 0
	with open(infile) as myfile:
        	cases=list(islice(myfile,1))
        	n = int(cases[0])
        for i in range(1,n+1):
        	print "Case#" + str(i)
        	with open(infile) as myfile:
			case = list(islice(myfile,i,i+1))
			case = case[0]
			case = case.split(" ")
			lastel = len(case) - 1
			l = len(case[lastel])-1	
			case[lastel] = case[lastel][0:l]

			print case

			g.write("Case #" + str(i) + ":" + " " + solve(case) + "\n")
				#"Case #" + str(j) + ":" + " " + str(solve(thiscase,j)) + "\n"
				#solve(thiscase,j)

grabproblem("in.txt","out.txt")
#solve(['0', '1', 'QW', '2', 'QW'])
