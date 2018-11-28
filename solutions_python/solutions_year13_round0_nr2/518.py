thefile = "B-large"
outputfile = open(thefile+".out","w")

with open(thefile+".in") as f:
	ff = [[int(x) for x in line.split()] for line in f]

def transpose(l):
	i=len(l)
	j=len(l[0])
	b = [[None for _ in range(i)] for _ in range(j)]
	for ii in range(j):
		for jj in range(i):
			b[ii][jj] = l[jj][ii]
	return b

def check(N,M,l):
	ll = transpose(l)
	row_max = [None for _ in range(N)]
	column_max = [None for _ in range(M)]
	for row in range(N):
		row_max[row] = max(l[row])
	for column in range(M):
		column_max[column] = max(ll[column])
	for i in range(N):
		for j in range(M):
			temp = min(row_max[i],column_max[j])
			if temp != l[i][j]:
				return "NO"
	return "YES"
		

pos = 1
for i in range(1,ff[0][0]+1):
	l = []
	for z in range(0,ff[pos][0]):
		l.append(ff[pos+1+z])
	outputfile.write("Case #%i: %s\n" % (i,check(ff[pos][0],ff[pos][1],l)))
	pos += ff[pos][0]+1

