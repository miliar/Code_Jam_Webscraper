#!usr/bin/python


filein = open("input.txt",'r')
fileout = open("output.txt",'w')

ffile = formater(filein)
c = 0
for e in ffile:
	c=c+1
	game_extender(e)
	fileout.write("Case #"+str(c)+": "+resulter(e)+"\n")
	print("Case #"+str(c)+": "+resulter(e))
fileout.close()


def formater(filein):
	rawlines = filein.readlines()
	formlines = []
	outlines = []
	for line in rawlines:
		formlines.append(line.strip())
	print(formlines)
	n = int(formlines[0])
	formlines.remove(formlines[0])
	print(formlines)
	for i in range(0,n):
		outlines.append(formlines[0:4])
		formlines.remove(formlines[0])
		formlines.remove(formlines[0])
		formlines.remove(formlines[0])
		formlines.remove(formlines[0])
		if len(formlines)!=0:
			formlines.remove(formlines[0])
	return outlines


def game_extender(game):
	game.append(""+game[0][0]+game[1][0]+game[2][0]+game[3][0])
	game.append(""+game[0][1]+game[1][1]+game[2][1]+game[3][1])
	game.append(""+game[0][2]+game[1][2]+game[2][2]+game[3][2])
	game.append(""+game[0][3]+game[1][3]+game[2][3]+game[3][3]) 
	game.append(""+game[0][0]+game[1][1]+game[2][2]+game[3][3])
	game.append(""+game[3][0]+game[2][1]+game[1][2]+game[0][3])

def resulter(game):
	dots=0
	for form in game:
		dots = dots+form.count(".")
		if form.count('X')==4:
			return "X won"
		if form.count('X')==3 and form.count('T')==1:
			return "X won"
		if form.count('O')==4:
			return "O won"
		if form.count('O')==3 and form.count('T')==1:
			return "O won"

	if dots==0:
		return "Draw"
	return "Game has not completed"


