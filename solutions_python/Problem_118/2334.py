import sys, os 
from math import sqrt

f = open(sys.argv[1], "r")
out = open("ce.out", "w")

def isPalindrome(n):
	return str(n) == str(n)[::-1]

for i in range (1,int(f.readline()[:-1])+1):
	(start, end) = f.readline()[:-1].split(" ")
	(start, end) = (int(start), int(end))

	count = 0
	for n in range(int(sqrt(start))-1, int(sqrt(end)+1)):
		if isPalindrome(n) and isPalindrome(n*n) and (n*n)<=end and (n*n)>=start:
			#print(n)
			count+=1
	
	print("Case #"+str(i)+": "+str(count))
	#print(start+end)

f.close()
out.close()
