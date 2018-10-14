import os

f = open("B-large.in",'r');
g = open("results.dat",'w')
f.readline()

text = f.readlines()
counter = 0;


for line in text:
	line = line.rstrip().split();
	counter = counter + 1
	combinecount = int(line[0])
	combine = line[1:(combinecount+1)]
	opposecount = int(line[combinecount+1])
	oppose = line[(combinecount+2):(combinecount+opposecount+2)]
	length = int(line[-2])
	word = line[-1]
	
	spell = []
	for i in range(len(word)):
		spell.append(word[i])
		if (len(spell) > 1):
			lasttwo = "".join(spell[-2:])
			for j in range(len(combine)):
				if ((combine[j][:2].find(lasttwo)!=-1)  or (combine[j][:2].find(lasttwo[::-1]) != -1)):
					spell.pop()
					spell.pop()
					spell.append(combine[j][2])
			curspell = "".join(spell)
			for j in range(len(oppose)):
				if ((curspell.find(oppose[j][0]) != -1) and (curspell.find(oppose[j][1])) != -1):
					spell = []
	spell = ", ".join(spell)
	g.write("Case #" + repr(counter) + ": [" + spell + "]\n")

f.close()
g.close()
	
			
			