def Xwon():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": X won\n")

def Owon():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": O won\n")

def Draw():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": Draw\n")

def NotDone():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": Game has not completed\n")

def line(line):
	if line[0]=='X':
		if (line[1]=='T' or line[1]=='X') and (line[2]=='T' or line[2]=='X') and (line[3]=='T' or line[3]=='X'):
			Xwon()
			return True		
	elif line[0]=='O':
		if (line[1]=='T' or line[1]=='O') and (line[2]=='T' or line[2]=='O') and (line[3]=='T' or line[3]=='O'):
			Owon()
			return True	
	elif line[0]=='T':
		if line[1]=='X':
			if line[2]=='X' and line[3]=='X':
				Xwon()
				return True	
		elif line[1]=='O':
			if line[2]=='O' and line[3]=='O':
				Owon()
				return True	
	return False
			
def test(t):
	for k in range(4):
		if line(t[k]):
			return
		if line([t[0][k],t[1][k],t[2][k],t[3][k]]):
			return
	if line([t[0][0],t[1][1],t[2][2],t[3][3]]):
		return
	if line([t[0][3],t[1][2],t[2][1],t[3][0]]):
		return
	for k in range(4):
		if '.' in t[k]:
			NotDone()
			return
	Draw()

# open input and output files
f = open('input','r')
g = open('output','w')

# for i 0...(N-1)
for i in range(int(f.readline())):
	
	# New test init
	t = []
	done = 0

	# Read in test line by line
	for j in range(4):
		tmp = f.readline()
		t +=[[tmp[0],tmp[1],tmp[2],tmp[3]]]
	
	test(t)
	f.readline()

f.close()
g.close()

