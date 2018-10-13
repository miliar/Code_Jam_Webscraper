infile = open('t.in', 'r')
fout = file('t.out', 'w')
def get_line():
	return infile.readline()

cases = int(get_line())



for q in range(cases):
	done = False
	charsets = int(get_line().rstrip('\n'))
	charseta = []
	chars = []
	order = ''
	for i in range(charsets):
		torder = ''
		charset = get_line().rstrip('\n')
		lastchar = ' '
		for char in charset:
			if not char == lastchar:
				torder += char
				lastchar = char
		if not order:
			order = torder
		else:
			if torder != order:
				if not done:
					fout.write("Case #"+str(int(q)+1)+': Fegla Won\n')
				done = True
		charseta.append(charset)
	if done: continue
	steps = 0
	for char in order:
		amnt = []
		for i in range(len(charseta)):
			bfore = len(charseta[i])
			charseta[i] = charseta[i].lstrip(char)
			bfore -= len(charseta[i])
			amnt.append(bfore)
		amntsteps = []
		for x in range(len(amnt)):
			amntsteps.append(0)
			for y in range(len(amnt)):
				if y == x:continue
				amntsteps[x] += abs(amnt[x] - amnt[y])
		amntsteps.sort()
		steps += amntsteps[0]
	fout.write("Case #"+str(int(q)+1)+': '+str(steps)+'\n')