import math

flist = []

def isPalindrome(n):
	n = str(n)
	length = len(n)
	#print length
	isPal = True
	for i in range(0,length/2):
		#print i
		#print n[i],n[length-i-1]
		if(n[i] != n[length-i-1]):
			isPal = False
			break
	#if(isPal): flist.append(n)
	return isPal

ffile = open('1.txt', 'w')
n = raw_input()
n = int(n)
for i in range(0,n):
	a = raw_input()
	b = a.split()
	a = int(b[0])
	b = int(b[1])
	count = 0
	#print a,(b+1)
	for j in range(a,b+1):
		k = math.sqrt(j)
		#print j,k,(k-int(k))
		if not k-int(k) > 0:
			if isPalindrome(j) and isPalindrome(int(k)):
				count += 1
	out = 'Case #'+str(i+1)+': '+str(count)
	ffile.write(out+'\n')