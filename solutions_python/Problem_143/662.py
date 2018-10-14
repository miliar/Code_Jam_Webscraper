import sys 

f = open('input.txt')
t=int(f.readline())

for j in range(0, t):
	a, b, k = [int(i) for i in f.readline().split()]
	c=0
	for i in range(0, a):
		for m in range(0, b):
			if (i&m<k):
				c+=1
	print "Case #"+str(j+1)+": "+str(c)
	
	
	
		
	