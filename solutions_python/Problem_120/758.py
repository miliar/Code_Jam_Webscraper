from math import *
pi = 3.14159265359

f = open('A.in', 'r')
l = open('A.out' , 'w')


T = int(f.readline())

for i in range(T):
	area = 0
	A = f.readline()
	B = A.split()
	R = int(B[0])
	t = int(B[1])
	n = 0
	while area <= t:
		area+= (R+1+2*n)**2 - (R+2*n)**2
		n+=1
		

	l.write("Case #"+str(i+1)+": "+str(n-1)+"\n")