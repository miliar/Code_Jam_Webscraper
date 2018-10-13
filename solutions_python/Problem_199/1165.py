from sys import stdin,stdout
from math import log,floor
t = int(stdin.readline())
for tc in range(t):
	cakes,k = stdin.readline().split()
	newCake = cakes
	k = int(k)
	impossible = 1
	flips = 0
	for i in range(len(cakes) - k + 1):
		a = set(newCake)
		if '+' in a and len(a) == 1:
			impossible = 0
			break
		
		if newCake[i] == '-':
			#print i
			#flip k characters
			flips += 1
			flippedString = ''
			for j in range(i,i+k):
				if newCake[j] == '-':
					flippedString +='+'
				else:
					flippedString +='-'
			s1 = newCake[:i]
			s2 = newCake[i+k:]
			newCake = s1 + flippedString + s2
			#print s1,flippedString,s2		
		a = set(newCake)	
		if '+' in a and len(a) == 1:
			impossible = 0
			break
	if impossible == 1:
		print "Case #{}: IMPOSSIBLE".format(tc+1)
	else:
		print "Case #{}: {}".format(tc+1,flips)