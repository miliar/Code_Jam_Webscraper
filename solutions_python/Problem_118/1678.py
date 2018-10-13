

def faireAndSquare(n): # check if faire-and-square
	w=n*n
	x=str(w)
	y=x[::-1]
	if(x==y): print(w) # print successfull result to screen

def palindromes(k, l): # recursively generate all palindromes from base number
	global number
	a=(k+1)//2
	if(l==a): return
	inc = 11*(10**l)
	if(l==a-1 and k%2):
		inc = 10**l
	for i in range(9):
		palindromes(k, l+1)
		faireAndSquare(number)
		number+=inc
	if(l!=0): palindromes(k, l+1)
	else: number=number-inc+2

number=1
def generateAll():
	global number
	k=1 # number of digits
	number=1
	while(True):
		palindromes(k, 0)
		k+=1
#generateAll()


def getCount(A, B):
	global FS
	count=0
	for i in FS:
		if(i>=A and i<=B):
			count+=1
	return count

FS=[]
f = open("listOfFairAndSquare.txt", "r")
for line in f:
	FS.append(eval(line))
f.close()

f = open("C-large-1.in", "r")
T=eval(f.readline())
for tcase in range(1,T+1):
	A, B = [int(x) for x in f.readline().split()]
	print("Case #", tcase, ": ", getCount(A,B), sep='')
f.close()


