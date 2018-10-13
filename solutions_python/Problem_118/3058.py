import math
def CheckFair(targetnumber):
	l =  0
	targetnumber = str(targetnumber) 
	h = len(targetnumber)-1
	while l <= h :
		if targetnumber[l] ==targetnumber[h]:
			l = l + 1
			h = h - 1
		else:
			return False	
	return True
def CheckFairSquare( targetnumber):
	if not CheckFair(targetnumber):
		return False
	targetnumber = int(targetnumber)
	root = int(math.sqrt(targetnumber))
	
	if not CheckFair(root) :
		return False
	if int(root + 0.5) ** 2 == targetnumber: 
		return True
	else:
		return False
F={}
F[0] = 0
F[1] = 1
for i in range(2,1000000):
	if CheckFairSquare(i) :
		F[i]= F[i-1]+1
	else:
		F[i] = F[i-1]
#print F
T = int(raw_input() )
C = {}
for i in range(0,T):
	readline = raw_input()
	numbers = readline.split(" ")
	A = int(numbers[0])
	B = int(numbers[1])
	j = i + 1
	C[i+1] = "Case #"+str(j)+": "+str(F[B]-F[A-1])
for i in C:
	print C[i]
