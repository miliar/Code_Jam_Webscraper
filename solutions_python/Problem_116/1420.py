from math import pow
import sys 

f=open(sys.argv[1], 'r' )
g=open(sys.argv[1].split(".")[0] +".out", 'w' )

def col_rows(x,who):
	_col = [0,0,0,0]
	_rows = [0,0,0,0]
	for i in range(0,len(x)):
		for j in range(0,len(x)):
			_col[j] +=equals(x[i][j],who)
			_rows[i]+=equals(x[i][j],who)
	return 4 in _col or 4 in _rows

def equals(p,who):
	return p==who or p=="T"

def diag(x, who):
	_diag = [0,0]
	for i in range(0,len(x)):
		_diag[0]+=equals(x[i][i],who)
		_diag[1]+=equals(x[i][len(x)-i-1],who)
	return _diag[0] == 4 or _diag[1] == 4

def checkWin(x,who):
	return col_rows(x,who) or diag(x,who)

def checkDraw(x):
	for i in x:
		for j in i:
			if (j=="."):
				return False
	return True

def output(c):
	print c
	g.write(c+"\n")

def analyze(x, which):
	s = "Case #"+str(which)+": ";
	O = checkWin(x,"O")
	X = checkWin(x,"X")
	if (X):
		output(s+"X won")
	elif (O):
		output(s+"O won")
	else:
		if checkDraw(x):
			output(s+"Draw")
		else:
			output(s+"Game has not completed")

line = -1
ile = f.readline()

for i in range(0,int(ile)):
	x = [0,0,0,0]
	for j in range(0,5):		
		if (j==4): 
			f.readline()
		else:
			x[j] = f.readline()
	analyze(x,i+1)
	
f.close()
g.close()