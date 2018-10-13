
fileout = open('output.out', 'w')
filein = open('B-large.in', 'r')

T = int(filein.readline()) #Number of cases
for i in range(T):
	N = int(filein.readline())

	strN = list(str(N))
	biggest = False;
	while(not biggest):
		biggest = True;
		for character in range(len(strN)-1, 0, -1):
			if(int(strN[character])<int(strN[character - 1])):
				biggest = False;
				strN[character] = '9'
				for x in range(len(strN)-1, character, -1):
					strN[x] = '9'
				print(strN[character-1])
				if(int(strN[character-1])==0):
					if(character-1 != 0):
						strN[character-1]= '9'
				else:
					strN[character-1] = str(int(strN[character-1]) - 1)
				if(character - 1 == 0 and int(strN[character-1])==0):
					strN.pop(0)
					break

	result = "".join(strN);

	fileout.write('Case #'+str(i+1)+': '+str(result)+'\n')



