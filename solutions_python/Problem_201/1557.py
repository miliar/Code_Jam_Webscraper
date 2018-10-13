filename = 'C-small-2-attempt2.in'
output	=	'output.txt'

openfile = open(filename, 'r')
outputfile = open(output, 'w')

openfile.readline()

spacesleft = []
availspaces = []


def addspace(a):
	if a in availspaces:
		spacesleft[availspaces.index(a)] = spacesleft[availspaces.index(a)] + 1
	else:
		availspaces.append(a)
		spacesleft.append(1)

def removespace(a):
	global spacesleft
	if a in availspaces:
		temp = availspaces.index(a)
		if spacesleft[temp] == 1:
			availspaces.remove(a)
			spacesleft = spacesleft[:temp] + spacesleft[temp + 1:]
		else:
			spacesleft[temp] = spacesleft[temp] - 1
	else:
		print str(a) + ' not in availspaces'

N = 0
K = 0
case = 1

for line in openfile:
	availspaces = []
	spacesleft = []	
	temp = [0,0]
	for a in range(0, len(line)):
		if line[a] == ' ':
			N = int(line[:a])
			K = int(line[a:])
			break
	addspace(N)

	for value in range(0, K):
		if N == K:
			temp = [0, 0]
			break
		spaces = max(availspaces)
		temp = [spaces/2, (spaces - 1)/2]
	
		addspace(temp[0])
		addspace(temp[1])
		removespace(spaces)		
		
	outputfile.write('Case #' + str(case) + ': ' + str(temp[0]) + ' ' + str(temp[1]) + '\n')
	print case
	case = case + 1