import sys

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	N = int(f.readline())
	strings = []
	for n in range(N):
		strings.append(f.readline())

	i = 0	
	count = 0
	fegla = False
	for s in range(len(strings[0])):
		if strings[0][s] == strings[1][i]:
			i = i + 1
			if (i >= len(strings[1])):
			 	if ((len(strings[0]) - s)*strings[0][s] == strings[0][s:]):
					count = count + (len(strings[0]) - s - 1)
				else:
					fegla = True
					break
		else:
			if s > 0:
				if strings[0][s] == strings[0][s-1]:
					count = count + 1
				elif strings[1][i] == strings[1][i-1]:
					j = 1
					while strings[1][i] == strings[1][i+j]:
						j = j + 1
					count = count + j
					i = i + j

					if strings[0][s] == strings[1][i]:
						i = i + 1
						if (i >= len(strings[1])):
							if ((len(strings[0]) - s)*strings[0][s] == strings[0][s:]):
								count = count + (len(strings[0]) - s - 1)
							else:
								fegla = True
								break
					else:
						fegla = True
						break

				else:
					fegla = True
					break
			else:
				fegla = True
				break

	if (not fegla) and (i < len(strings[1])):
		if (strings[1][i] == strings[0][-1]) and ((len(strings[1]) - i)*strings[1][i] == strings[0][i:]):
			count = count + (len(strings[1]) - i)
		else:
			fegla = True

	if fegla:
		print 'Case #'+str(t+1)+': Fegla Won'
	else:
		print 'Case #'+str(t+1)+': '+str(count)



