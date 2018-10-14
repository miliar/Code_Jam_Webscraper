import math

def check(l):
	symetric=True
	i=0
	length=len(l)
	while symetric and i<=length/2.:
		if l[i]!=l[-1-i]:
			return False
		i=i+1
	return True

def count(A,B,j):
	number=0
	C,D=int(math.ceil(math.sqrt(A))),int(math.sqrt(B))+1
	for i in range(C,D):
		if check(str(i)):
			if check(str(i**2)):
				number=number+1
	print "Case #"+str(j+1)+": "+str(number)

f=open("C-small-attempt0.in")
T=f.readline()
for i in range(int(T)):
	line=f.readline().split()
	A,B=int(line[0]),int(line[1])
	count(A,B,i)
