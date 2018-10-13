f = open('A-large.in', 'r')
input = f.read()
f.close()

if input[3] != '\n' and  input[3] != '.'  and  input[3] != 'O'  and  input[3] != 'X':
	nbtest = int(input[0] + input[1] + input[2] + input[3])
	offset = 4
elif input[2] != '\n' and  input[2] != '.'  and  input[2] != 'O'  and  input[2] != 'X':
	nbtest = int(input[0] + input[1] + input[2])
	offset = 3
elif input[1] != '\n' :
	nbtest = int(input[0] + input[1])
	offset = 2
else :
	nbtest = int(input[0])
	offset = 1
	
i = 0
grilles = []
print(nbtest)
while i < nbtest :
	j = 0
	grilles.append([])
	while j < 16 :
		if input[offset] == '\n' :
			pass
		elif input[offset] == 'O' :
			grilles[i].append(0)
			j += 1
		elif input[offset] == 'X' :
			grilles[i].append(1)
			j += 1
		elif input[offset] == 'T' :
			grilles[i].append(2)
			j += 1
		elif input[offset] == '.' :
			grilles[i].append(3)
			j += 1
		offset += 1
	i += 1
	
out = open('output_tictactoe.txt', 'w')
for x in xrange(nbtest) :

	'''print('tableau ' + str(x) + ' : '),
	for y in xrange(16) :
		print(grilles[x][y]),
	print(' ')'''
	
	Xresult = []
	Oresult = []
	for pos in xrange(4) :
		if grilles[x][pos * 4 + pos] == 0 :
			Oresult.append(0)
		elif grilles[x][pos * 4 + pos] == 1 :
			Xresult.append(1)
		elif grilles[x][pos * 4 + pos] == 2 :
			Oresult.append(0)
			Xresult.append(1)
	if len(Xresult) == 4 :
		out.write('Case #' + str(x + 1) + ': X won\n')
		continue
	elif len(Oresult) == 4 :
		out.write('Case #' + str(x + 1) + ': O won\n')
		continue
		
	Xresult = []
	Oresult = []
	for pos in xrange(4) :
		if grilles[x][pos * 4 + 3 - pos] == 0 :
			Oresult.append(0)
		elif grilles[x][pos * 4 + 3 - pos] == 1 :
			Xresult.append(1)
		elif grilles[x][pos * 4 + 3 - pos] == 2 :
			Oresult.append(0)
			Xresult.append(1)
	if len(Xresult) == 4 :
		out.write('Case #' + str(x + 1) + ': X won\n')
		continue
	elif len(Oresult) == 4 :
		out.write('Case #' + str(x + 1) + ': O won\n')
		continue
	
	stop = 0
	for line in xrange(4) :
		if stop == 1 :
			break
		Xresult = []
		Oresult = []
		for pos in xrange(4) :
			if grilles[x][line * 4 + pos] == 0 :
				Oresult.append(0)
			elif grilles[x][line * 4 + pos] == 1 :
				Xresult.append(1)
			elif grilles[x][line * 4 + pos] == 2 :
				Oresult.append(0)
				Xresult.append(1)
		if len(Xresult) == 4 :
			out.write('Case #' + str(x + 1) + ': X won\n')
			stop = 1
			continue
		elif len(Oresult) == 4 :
			out.write('Case #' + str(x + 1) + ': O won\n')
			stop = 1
			continue
	if stop == 1 :
		continue
	
	for col in xrange(4) :
		if stop == 1 :
			break
		Xresult = []
		Oresult = []
		for pos in xrange(4) :
			if grilles[x][col + pos * 4] == 0 :
				Oresult.append(0)
			elif grilles[x][col + pos * 4] == 1 :
				Xresult.append(1)
			elif grilles[x][col + pos * 4] == 2 :
				Oresult.append(0)
				Xresult.append(1)
		if len(Xresult) == 4 :
			out.write('Case #' + str(x + 1) + ': X won\n')
			stop = 1
			continue
		elif len(Oresult) == 4 :
			out.write('Case #' + str(x + 1) + ': O won\n')
			stop = 1
			continue
	if stop == 1 :
		continue
		
	for pos in xrange(16) :
		if grilles[x][pos] == 3 :
			stop = 1
			break
	if stop == 1 :
		out.write('Case #' + str(x + 1) + ': Game has not completed\n')
	else :
		out.write('Case #' + str(x + 1) + ': Draw\n')
out.close()		