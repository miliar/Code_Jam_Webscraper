def getcandidates(x):
	t = open('magician.txt','r')
	for i,line in enumerate(t):
		if i == x:
			return [int(a) for a in line.split(' ')]

def readlines(x):
	reading = {}
	t = open('magician.txt','r')
	for i,line in enumerate(t):
		line = line.strip('\n')
		if i == x:
			reading[1]=[int(a) for a in line.split(' ')]
		elif i == (x+1):
			reading[2]=[int(a) for a in line.split(' ')]
		elif i == (x+2):
			reading[3]=[int(a) for a in line.split(' ')]
		elif i == (x+3):
			reading[4]=[int(a) for a in line.split(' ')]
	return reading

def convertpos(x):
	return (x-1)*10+1

variants = getcandidates(0)
print variants[0]

container = {}
for a in range(1,variants[0]+1):
	pos = convertpos(a)
	column1 = getcandidates(pos)[0]
	column2 = getcandidates(pos+5)[0]
	container[a] = {}
	container[a]['first'] = set(getcandidates(pos+column1))
	container[a]['second'] = set(getcandidates(pos+5+column2))
print container

# generate output file
wf = open('output.txt','w')
for c in container:
	string = "Case #"+str(c)+': '
	resulting = container[c]['first'].intersection(container[c]['second'])
	if len(resulting) == 0:
		# no mutual number:
		string += 'Volunteer cheated!\n'
	elif len(resulting) > 1:
		# more than one candidate
		string += 'Bad magician!\n'
	elif len(resulting) == 1:
		# number found
		string += str(list(resulting)[0])+'\n'
	wf.write(string)
wf.close()

