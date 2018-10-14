import sys

f = open('C:\\Users\\Daniel\\Desktop\\C-small-attempt0.in')

N = int(f.readline())

def palindrome(x):
	x = str(x)
	if x=='' or len(x)==1:
		return True
	elif x[0]!=x[-1]:
		return False
	else:
		return palindrome(x[1:-1])


dct = [i**2 for i in range(10**7+1) if palindrome(i) and palindrome(i**2)]

def neighbour(x):
	for i in range(len(dct)):
		if dct[i]>=x:
			return i
	return len(dct)-1

for n in range(1, N+1):
	count = 0
	a,b = map(int, f.readline().strip().split())
	print "Case #" +str(n) + ": " + str(neighbour(b+1)-neighbour(a))
