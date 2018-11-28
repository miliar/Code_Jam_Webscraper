lower = 1
upperpower = 100
upper = 10**upperpower
halfpower = upperpower//2
halfupper = 10**halfpower

squarepalindromes = [1,4,9]
#roots = []

from math import sqrt

def ispalindrome(n):
	s = str(n)
	return s == s[::-1]
	
def search(n):
	low = 0
	high = len(squarepalindromes)
	
	mid = (low+high)//2
	
	while low < mid:
		if squarepalindromes[mid] <= n:
			low = mid
		else:
			high = mid-1
		mid = (low+high)//2
	
	print(low,mid,high)
	return mid
	
def case():
	a,b = map(int,input().split())
	"""print(a,b)
	low = search(a)
	high = search(b)
	print(low,high)
	print(squarepalindromes[low], squarepalindromes[high])
	print(high-low + (1 if squarepalindromes[low] == a else 0))
	print(len( list( filter(lambda n: a <= n and n <= b, squarepalindromes) ) ))"""
	return len( list( filter(lambda n: a <= n and n <= b, squarepalindromes) ) )
	
def generate(s):
	if len(s) <= halfpower:
		if len(s) > 1 and s[0] != "0":
			i = int(s)
			i = i*i
			if ispalindrome(i):
				squarepalindromes.append(i)
				#roots.append(s)
	if len(s) < halfpower-1:
		generate("0"+s+"0")
		generate("1"+s+"1")
	
def generateiempty(n, power, nonZeroStart):
	if n <= halfupper:
		if n >= 10 and nonZeroStart:
			i = n*n
			if ispalindrome(i):
				squarepalindromes.append(i)
				#roots.append(n)
	#if len(s) < halfpower-1:
		if power <= halfupper:
			generateiempty(n*10, power*100, False)
			generateiempty(power+n*10+1, power*100, True)

def generatei(n, power, nonZeroStart):
	if n <= halfupper:
		if n >= 10 and nonZeroStart:
			i = n*n
			if ispalindrome(i):
				squarepalindromes.append(i)
				#roots.append(n)
	#if len(s) < halfpower-1:
		if power <= halfupper:
			generatei(n*10, power*100, False)
			generatei((power+n)*10+1, power*100, True)
	
def preprocess():
	for i in range(2,halfpower+1):
		squarepalindromes.append( int( "2" + (i-2)*"0" + "2" )**2 )
		if i % 2 == 1:
			squarepalindromes.append( int( "2" + (i//2-1)*"0" + "1" + (i//2-1)*"0" + "2" )**2 )
	
			
preprocess()
#generate("")
generateiempty(0,10,False)
#print(len(squarepalindromes))
for i in range(0,3):
	#generate(str(i))
	generatei(i,10,False)
	#print(i,len(squarepalindromes))
squarepalindromes.sort()
for t in range(1,int(input())+1):
	print ( "Case #%d: %d" % (t,case()) )

