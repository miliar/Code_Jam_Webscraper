from math import pow
import sys 

f=open(sys.argv[1], 'r' )
g=open(sys.argv[1].split(".")[0] +".out", 'w' )

def output(c):
	print c
	g.write(c+"\n")

def printLawn(x,n,m):
	for i in range(0,n):
		for j in range(0,m):
			sys.stdout.write(str(x[i][j]) + " ")
			g.write(str(x[i][j]) + " ")
		print ""
		g.write("\n")
def findLowest(x,n,m,higher):
	low = 100
	for i in range(0,n):
		for j in range(0,m):
			if x[i][j]<=low and x[i][j]>higher:
				low = x[i][j]
	return low

def checkRow(x,n,m,ind,low,lower):
	for i in range(0,m):
		if not (x[ind][i]==low or x[ind][i] in lower):
			return False
	return True

def checkCol(x,n,m,ind,low,lower):
	for i in range(0,n):
		if not (x[i][ind]==low or x[i][ind] in lower):
			return False
	return True

def checkLowest(low,n,m,lower):
	indx = []
	indy = []
	for i in range(0,n):
		for j in range(0,m):
			if (x[i][j]==low):
				rowOrCol = False
				rowOrCol = (rowOrCol or checkRow(x,n,m,i,low,lower))
				rowOrCol = (rowOrCol or checkCol(x,n,m,j,low,lower))
				if (not rowOrCol):
					return False
	return True

def analyze(x,which,n,m):
	# printLawn(x,n,m)
	s = "Case #"+str(which)+": ";
	lower = [0]
	
	works= True
	while(works):
		low=findLowest(x,n,m,lower[-1])
		if (low == 100):
			output(s+"YES")
			return
		works = checkLowest(low,n,m,lower)
		if (not works):
			output(s+"NO")
			return
		lower.append(low)
	

ile = f.readline()
for i in range(0,int(ile)):
	[n,m] = map(int, f.readline().split(" "))
	x=[]
	for j in range(0,n):		
		x.append(map(int, f.readline().split()))
	
	analyze(x,i+1,n,m)
	
f.close()
g.close()