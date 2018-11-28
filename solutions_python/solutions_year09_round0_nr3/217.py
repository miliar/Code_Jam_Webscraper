#dynamic programming

pat = "welcome to code jam"
n = len(pat)

		
def Count(str):
	N = len(str)
	row = [0]*(n+1) #each row is a pat
	table = []
	for i in range(N+1):
		table.append(row[:])
	#table = row*(N+1) #each col is a str
	#print table
	for i in range(N+1):
		table[i][0] = 1
	for i in range(1,N+1): #str
		for j in range(1,n+1):#pat
			if str[i-1]==pat[j-1]:
				table[i][j]=table[i-1][j-1]+table[i-1][j]
			else:
				table[i][j]=table[i-1][j]
	return table[N][n]
	
	


if __name__ == '__main__':
	INFILE = 'C-small-attempt2.in'
	IN = open(INFILE)
	LINE = IN.readline()
	DATA = LINE.split()
	N = int(DATA[0]) #number of tests
	for i in range(N):
		LINE = IN.readline()
		ct = Count(LINE)
		print 'Case #%d: %.4d'%(i+1, ct)
