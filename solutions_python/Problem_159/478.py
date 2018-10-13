
from sys import argv

fname = argv[1]
f = open(fname, 'r')

content = f.read().split('\n')


ncases = int(content[0])

for ncase in range(1, 1 + ncases):
	
	temp = int(content[ncase*2 -1])
	mushs = content[ncase*2].split(' ')
	
	eaten1 = 0
	maxdiff = 0
	for i in range(len(mushs)-1):
		mdiff = int(mushs[i]) - int(mushs[i+1])
		if mdiff > 0:
			eaten1 += mdiff
		if mdiff > maxdiff:
			maxdiff = mdiff
		
	eaten2 = 0
	for i in range(len(mushs)-1):
		if int(mushs[i]) <= maxdiff:
			eaten2 += int(mushs[i])
		if int(mushs[i]) > maxdiff:
			eaten2 += maxdiff
		
	print('Case #%d: %d %d' % (ncase, eaten1, eaten2))
		
