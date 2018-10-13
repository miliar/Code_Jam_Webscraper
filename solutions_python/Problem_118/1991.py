import math
f = open('C-small-attempt0.in')
f=f.read().splitlines()
cases = int(f[0]) # number of cases in the file

f = [x.split() for x in f ]

def isFaF(n):
	sroot = math.sqrt(n)
	if sroot - int(sroot) != 0:
		return False
	rIsPal = str(int(sroot)) == str(int(sroot))[::-1]
	isPal = (str(n)[::-1] == str(n)) #  is n a palindrome
	if (isPal and rIsPal):
		return True
	return False

ans=""
case = 0
for i in range(1, cases+1):
	case += 1
	A = int(f[i][0])
	B = int(f[i][1])
	count = 0
	for i in range(A, B+1):
		if isFaF(i):
			count += 1
	ans += "Case #" + str(case) +": " + str(count) + '\n'
print ans
a=open('small.txt','w')
a.write(ans)
