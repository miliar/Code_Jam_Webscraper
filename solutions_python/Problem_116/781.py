import re
def detStat(board):
	XWON='X won'
	OWON='O won'
	DRAW='Draw'
	CONT='Game has not completed'
	count=0
	for i in range(4):
		row=b[i]
		count=count+4-len(re.findall(r'\.',row))
		column=''.join([b[j][i] for j in range(4)])
		#print row,column
		if row.count('X')==4 or column.count('X')==4 or\
		((row.count('X')==3) and 'T' in row) or\
		((column.count('X')==3) and 'T' in column):
			return XWON

		if row.count('O')==4 or column.count('O')==4 or\
		((row.count('O')==3) and 'T' in row) or\
		((column.count('O')==3) and 'T' in column):
			return OWON
	diag1=''.join([b[0][0],b[1][1],b[2][2],b[3][3]])
	diag2=''.join([b[0][3],b[1][2],b[2][1],b[3][0]])
	
	if diag1.count('X')==4 or diag2.count('X')==4 or\
	((diag1.count('X')==3) and 'T' in diag1) or\
	((diag2.count('X')==3) and 'T' in diag2):
		return XWON

	if diag1.count('O')==4 or diag2.count('O')==4 or\
	((diag1.count('O')==3) and 'T' in diag1) or\
	((diag2.count('O')==3) and 'T' in diag2):
		return OWON

	if count==16:
		return DRAW
	else:
		return CONT


f=open("./large.txt")
#t number of games
t=int(f.readline()[:-1])
with open('./out.txt','w') as fout:
	for i in range(1,t+1):
		b=[]
		for j in range(0,4):
			if i==t and j==3:
				b.append(f.readline())
			else:
				b.append(f.readline()[:-1])
		temp=f.readline()
		status=detStat(b)
		str='Case #%i: %s\n' %(i,status)
		fout.write(str)

