def solve(lnum,N,S,p,totalScores):
	num=0
	i=0
	s=0
	while i < N:
		picked = False

		if totalScores[i] == 0:
			if p == 0:
				num += 1
			i += 1
			continue

		if totalScores[i] % 3 == 1 and totalScores[i]/3+1 >= p:
			num += 1

		elif totalScores[i] % 3 == 2:
			if totalScores[i]/3+1 >= p:
					num += 1
					picked = True

			if picked == False and s < S:
				if totalScores[i]/3+2 >= p:
					num += 1
					s += 1
			
		else:
			if totalScores[i]/3 >= p:
					num += 1
					picked = True
			if picked ==  False and s < S:
				if totalScores[i]/3+1 >= p:
					num += 1
					s += 1
			
		i += 1
		
	print "Case #{n}: {a}".format(n=lnum,a=num)					


def solveProblem(lnum,line):
	i=0
	j=0
	N = 0
	S = 0
	p = 0
	while i < 3:
		num = ''
		while line[j] != ' ':
			num += line[j]
			j = j + 1
		if i == 0:
			N = int(num)
		elif i == 1:
			S = int(num)
		else:
			p = int(num)
		i += 1
		j += 1
	
	i = 0
	totalScores=[]
	while i < N:
		num = ''
		while line[j] != ' ' and line[j] != '\n':
			num += line[j]
			j = j + 1
		totalScores.append(int(num))
		i += 1
		j += 1
	solve(lnum,N,S,p,totalScores)



inputFile = open ( 'B-large.in', 'r')

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