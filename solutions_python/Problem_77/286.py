f = open('D-large.in', 'r')
g = open('Case1soln.dat', 'w')
g.close()
g = open('Case1soln.dat', 'a')
NumCases=int(f.readline())
for i in range (1,2*NumCases+1):
	line=f.readline().rstrip()
	words=line.split(' ')
	numlist=[]

	if i%2==1:
		size=int(line)
	else:
		for j in range(0,size):
			if int(words[j])!=j+1:
				numlist.append(int(words[j]))
		#print float(len(numlist))
		g.write('Case #' + str(i/2) + ': ' + str(float(len(numlist))) + '\n')
