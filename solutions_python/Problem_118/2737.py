import math

palindromeMap=dict()
hits=0

def isPalindrome(s):
	global hits
	if s in palindromeMap:
		hits+=1
		return palindromeMap[s]

	l=len(s)

	for x in xrange(len(s)):
		if s[x]!=s[l-x-1]:
			palindromeMap[s]=False
			return False

	palindromeMap[s]=True
	return True

def isSquare(n):
	a=math.sqrt(n)
	return (a - int(a))==0

def solve(vals):
	possibles=[]
	a=vals[0]
	b=int(vals[1])
	sqrta=math.sqrt(int(a))
	if(sqrta==int(sqrta)):
		ar=sqrta
	else:
		ar=int(sqrta)+1

	vr=ar
	while(vr*vr<=b):
		if(isPalindrome(str(int(vr)))):
			possibles+=[str(int(vr*vr))]
		vr=vr+1


	palindromes=filter(lambda x: isPalindrome(x),possibles)
	resp=len(palindromes)
	return resp 

def main():
	global hits
	file=open('input.txt')
	size=file.readline()
	for x in xrange(int(size)):
		line=file.readline().replace('\n','')
		vals=line.split(' ')
		resp=solve(vals)
		print "Case #" + str(x+1) + ": " + str(resp)


main()