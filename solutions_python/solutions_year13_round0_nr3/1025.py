#Fair and Square
from math import * 

def isPalindrome(num):
	for i in range(len(num)):
		if num[i] != num[-i - 1]:
			return False
	return True

f = open("C-small-attempt0.in")
p = open("Out.out", "w+")
T = f.readline()
results = []
for i in range(int(T)):
	bounds = f.readline().strip("\n").split(' ')
	A = int(bounds[0])
	B = int(bounds[1])
	lBound = ceil(sqrt(A))
	uBound = floor(sqrt(B))
	numFandS = 0
	print("lBound = " + str(lBound))
	print("uBound = " + str(uBound))
	for j in range(lBound,uBound + 1):

		if (isPalindrome(str(j)) and isPalindrome(str(j**2))):
			numFandS += 1
			print("Case #" + str(i+1) + ": " + str(j**2))
	results.append("Case #" + str(i+1) + ": " + str(numFandS))

print(results)
for line in results:
	p.write(line + "\n")