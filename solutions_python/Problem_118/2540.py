import sys
import math

class NumRange:
	A=0
	B=0
	caseId=0
	FairSquareOut="Case #%d: %d"

	def IsPalindrome(self,i):
		istr=str(i)
		m=len(istr)/2
		n=m if (len(istr)%2==0) else m+1
		if(istr[:m]==istr[n:]):
			return True
		else:
			return False

	def QuickLookForSquare(self,i):
		if(i%3==2 or i%10 in [2,3,7,8]):
			return False
		else: 
			return True

	def IsSquare(self,i):
		if(self.QuickLookForSquare(i)):
			n=int(math.sqrt(i))
			return (n*n==i,n)
		else:
			return (False,0)

	def GetFairSquareCount(self):
		i=self.A
		j=self.B
		n=0
		while i<=j:
			t=self.IsSquare(i)
			if t[0]:
				if (self.IsPalindrome(i) and self.IsPalindrome(t[1])):
					n=n+1
			i=i+1
		return self.FairSquareOut%(self.caseId,n)

	def __init__(self,id,a,b):
		self.caseId=id
		self.A=a
		self.B=b

def AnalyzeCases(cases):
	for c in cases:
		print c.GetFairSquareCount()

def ParseLines(allLines):
	n=int(allLines[0])
	i=1
	cases=[]
	while i<=n:
		l=allLines[i]
		a,b=l.split()
		cases.append(NumRange(i,int(a),int(b)))
		i=i+1
	return cases

def ReadFile(name):
	f=open(name)
	allLines=f.readlines()
	f.close()
	return allLines

def main():
	allLines=ReadFile(sys.argv[1])
	cases=ParseLines(allLines)
	AnalyzeCases(cases)

if __name__ == '__main__':
	main()