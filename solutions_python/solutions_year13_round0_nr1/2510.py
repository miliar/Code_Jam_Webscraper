class TicTac():
	blen=range(4)
	def __init__(self,inBoardStr):
		self.board=[]
		for (crow,cline) in zip(self.blen,inBoardStr.split('\n')):
			cbline=[clet.upper() for (ccol,clet) in zip(self.blen,cline)]
			self.board+=[cbline]
	def checkwin(self):
		if self.checkvic('X'): return 'X won'
		if self.checkvic('O'): return 'O won'
		if self.notfinished(): return 'Game has not completed'
		else: return 'Draw'
	def notfinished(self):
		isEmpty=lambda x: x=='.'
		return any(map(lambda cline: any(map(isEmpty,cline)),self.board))
	def checkvic(self,val):
		if any(map(lambda i: self.checkvicr(val,i),self.blen)): return True
		if any(map(lambda i: self.checkvicc(val,i),self.blen)): return True
		if any(self.checkvicd(val)): return True
		return False
	def checkvicr(self,val,i):
		isFull=lambda x: (x==val) | (x=='T')
		oVals=map(isFull,self.board[i])
		print ('r',val,i,oVals)
		return all(oVals)
	def checkvicc(self,val,i):
		isFull=lambda x: (x==val) | (x=='T')
		oVals=map(lambda cline: isFull(cline[i]),self.board)
		print ('c',val,i,oVals)
		return all(oVals)
	def checkvicd(self,val):
		isFull=lambda x: (x==val) | (x=='T')
		diagA=zip(self.blen,self.blen)
		diagB=zip(self.blen[::-1],self.blen)
		checkVals=lambda diag: all(map(lambda cc: isFull(self.board[cc[0]][cc[1]]),diag))
		oVals=map(checkVals,[diagA,diagB])
		print (val,oVals)
		return oVals
	def __str__(self):
		return str(self.board)

f=open('/mnt/sdcard/Download/A-large.in','r')
bds=int(f.readline())
oList=[]
for i in range(bds):
	cboard=map(lambda x: f.readline(),range(4))
	f.readline()
	oList+=[TicTac(''.join(cboard))]
f.close()
winList=map(lambda x: x.checkwin(),oList)
f=open('/mnt/sdcard/Download/tictacout5.txt','w')

for (caseN,status) in enumerate(winList): f.write('Case #%i: %s\n' % (caseN+1,status))
f.close()
#b=TicTac('..XO\nX.TX\n.O.T\nOXXO')

#print b.checkwin()
