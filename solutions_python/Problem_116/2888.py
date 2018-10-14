def se(a,b):
	if a=="." or b ==".":
		return False
	if a=="T" or b=="T":
		return True
	return a==b


def checkcomp(table):
	for rowi in range(4):
		for col in table[rowi]:
			if col==".":
				return False
	return True


def colof(table,i):
	return [item[i] for item in table]


def solveHor(table):		
	for rowi in range(4):
		line=table[rowi]
		res=True
		ch=line[0]
		if line[0]=="T":
			ch=line[1]
		for li in range(4):
			res=res & se(line[li],ch)
		if res:
			return ch
	return "N"		


def solveVer(table):
	for row in range(4):
		line=colof(table,row)
		res=True
		ch=line[0]
		if line[0]=="T":
			ch=line[1]
		for li in range(4):
			res=res & se(line[li],ch)
		if res:
			return ch
	return "N"



def solveDia(table):
	ch=table[0][0]
	if ch=="T":
		ch==table[1][1]
	res=True
	for i in range(4):
		res = res & se(table[i][i],ch)
	if res:
		return ch	
	ch=table[0][3]
	if ch=="T":
		ch==table[1][2]
	res=True
	for i in range(4):
		res = res & se(table[i][3-i],ch)
	if res:
		return ch	
	return "N"
	
	
def solve(table):
	sh=solveHor(table)
	if sh=="X" or sh=="O":
		return sh+" won"
	sv=solveVer(table)
	if sv=="X" or sv=="O":
		return sv+" won"	
	sd=solveDia(table)
	if sd=="X" or sd=="O":
		return sd+" won"
	if not checkcomp(table):
		return "Game has not completed"
	return "Draw"


def readCase(f,casenum):
	table=[]
	for i in range(4):	
		table.append(list(f.readline())[:4])
	f.readline()
	print "Case #"+str(casenum)+": "+solve(table)

def main():
	f=open('input.in','r')
	num=f.readline()
	num=int(num)
	for i in range(num):
		readCase(f,(i+1))

main()
