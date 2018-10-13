import sys

f = open(sys.argv[1])

N = int(f.readline())

def palindrome(x):
	x = str(x)
	if x=='' or len(x)==1:
		return True
	elif x[0]!=x[-1]:
		return False
	else:
		return palindrome(x[1:-1])


dct = set([i**2 for i in range(10**7+1) if palindrome(i)])


for n in range(1, N+1):
	count = 0
	a,b = map(int, f.readline().strip().split())
	i = a
	while(i<=b):
		if i in dct:
			if palindrome(i):
				count +=1
		i+=1
	print "Case #" +str(n) + ": " + str(count)
