

def solve(lawn,n,m):
	maxRows=[]
	maxCols=[]
	for line in lawn:
		maxRows+=[max(line)]
	for x in xrange(m):
		col=[]
		for y in xrange(n):
			col+=[lawn[y][x]]
		maxCols+=[max(col)]


	for r in xrange(n):
		for c in xrange(m):
			if(lawn[r][c] not in [maxCols[c],maxRows[r]]):
				return "NO"

	return "YES"


def main():
	f=open('input2.txt')
	size=int(f.readline())
	for x in xrange(size):
		size=f.readline().replace('\n','')
		(n,m)=size.split(' ')
		n=int(n)
		m=int(m)
		lawn = [0 for h in xrange(n)] 
		for i in xrange(n):
			line=f.readline().replace('\n','')
			lawn[i]=line.split(' ')
		val=solve(lawn,n,m)
		print "Case #" + str(x+1) + ": " + val



main()