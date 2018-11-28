#------------------------------------------------------------------------------#
# Author: Abhishekam N Swamy
# Google Code Jam - 2013 Qualification Round
# Represents a single case in the Tac Tack Toe problem -
#------------------------------------------------------------------------------#
class GameState:
	""" Represents the current state of the game
	"""
	nRows=4
	nColumns=4
	caseId=0
	winLines=[]
	state='Case #%d: %s'
	winStatus='%s won'
	drawStatus='Draw'
	incompleteStatus='Game has not completed'

	def lCircShift(self,l):
		newl=l[1:]+l[0]
		return newl

	def WhosTheWinner(self,l):
		if l==self.lCircShift(l):
			return((True,l[0]))
		else:
			return((False,''))

	def GetState(self):
		inComplete=False
		for l in self.winLines:
			if '.' not in l:
				t=self.WhosTheWinner(l)
				if(t[0]):
					return self.state%(self.caseId,self.winStatus%(t[1]))
			else:
				inComplete=True
		if(inComplete):
			return self.state%(self.caseId,self.incompleteStatus)
		else:
			return self.state%(self.caseId,self.drawStatus)

	def AddToWinLines(self,l):
		if l not in self.winLines:
			self.winLines.append(l)

	def CleanTs(self):
		clean=[]
		for l in self.winLines:
			if 'T' in l:
				i=l.index('T')
				newX=l[:i]+'X'+l[i+1:]
				newO=l[:i]+'O'+l[i+1:]
				clean.append(newX)
				clean.append(newO)
			else:
				clean.append(l)
		self.winLines=clean

	def RDiagonal(self,lines):
		l=''
		i=0
		j=self.nColumns-1
		while i<self.nRows:
			l=l+lines[i][j]
			i=i+1
			j=j-1
		self.AddToWinLines(l)

	def LDiagonal(self,lines):
		l=''
		for i in range(self.nRows):
			l=l+lines[i][i]
		self.AddToWinLines(l)

	def Columns(self,lines):
		for i in range(self.nRows):
			l=''
			for j in range(self.nColumns):
				l=l+ lines[j][i]
			self.AddToWinLines(l)

	def Rows(self,lines):
		for l in lines:
			self.winLines.append(l);

	def InitWinLines(self,lines):
		self.winLines=[]
		self.Rows(lines)
		self.Columns(lines)
		self.LDiagonal(lines)
		self.RDiagonal(lines)
		self.CleanTs()

	def __init__(self,caseId,lines):
		self.caseId=caseId
		self.InitWinLines(lines)

if __name__ == '__main__':
	cases=[
			['XXXT', '....', 'OO..', '....'], 
			['XOXT','XXOO','OXOX','XXOO'],
			['XOX.', 'OX..', '....', '....'],
			['OOXX', 'OXXX', 'OX.T', 'O..O'],
			['XXXO', '..O.', '.O..', 'T...'],
			['OXXX', 'XO..', '..O.', '...O']
		]
	caseId=1
	games=[] 
	for c in cases:
		g= GameState(caseId,c)
		games.append(g)
		caseId+=1
	for g in games:
		print g.GetState()


