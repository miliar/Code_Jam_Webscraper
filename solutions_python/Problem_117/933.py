def maxinrow(lawn,n,m,row):
	maxinrow = 0
	for i in range(0,m):
		if lawn[row][i] > maxinrow:
			maxinrow = lawn[row][i]
	return maxinrow

def maxincol(lawn,n,m,col):
	maxincol = 0
	for i in range(0,n):
		if lawn[i][col] > maxincol:
			maxincol = lawn[i][col]
	return maxincol

def cut(lawn,n,m):
	for i in range(0,n):
		for j in range(0,m):
			if lawn[i][j] < maxincol(lawn,n,m,j):
				if lawn[i][j] < maxinrow(lawn,n,m,i):
					return 'NO'

	return 'YES'


## Main
f = open('B-large.in')
## Read the first line 
line = f.readline()
t = int(line)

k=0
while k<t:
	nm = f.readline().split()
	n = int(nm[0])
	m = int(nm[1])
	lawn = [[0 for col in range(m)] for row in range(n)]
	i=0
	while i<n:
		line = f.readline()
		aux = line.split()
		j=0
		for a in aux:
			lawn[i][j]= int(a)
			j=j+1
		i=i+1
	print 'Case #'+ str(k+1) + ': ' + cut(lawn,n,m)
	k=k+1
f.close()
