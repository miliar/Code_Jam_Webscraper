import sys
from math import ceil, floor
def CFairAndSquare(InputFileName):
	OutputFileName=InputFileName.replace('.in','out')
	lines = open(InputFileName).read().splitlines()
	f = open(OutputFileName,'w')
	T=int(lines[0])
	for t, line in enumerate(lines[1:]):
		A,B=map(int, line.split())
		count=0
		for i in [k for k in range(int(ceil(A**0.5)),int(floor(B**0.5))+1) if IsPalindrome(str(k)) and IsPalindrome(str(k**2))]:
			#print i, i**2
			count+=1
		print('Case #'+str(t+1)+': ' + str(count)) #,file=f)
def IsPalindrome(StrTestD):
	if StrTestD==StrTestD[::-1]: return True
	else: return False	 
def main():	
	if len(sys.argv)==2: FileName=sys.argv[1]
	else: FileName='C-example.in'
	CFairAndSquare(FileName)
if __name__ == '__main__':
	main()
	
