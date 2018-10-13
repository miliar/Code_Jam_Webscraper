import math
f = open("c.in")
of = open("c.out","w")
T = int(f.readline())
for i in range(T):
	A,B = map(int,f.readline().split(' '))
	#take the sqrt of the left and the sqrt of the right
	left = int(math.sqrt(A))
	right = int(math.sqrt(B))+1
	count = 0
	for j in range(left,right+1):
		if str(j) == str(j)[::-1]:
			if str(j**2) == str(j**2)[::-1] and j**2 >= A and j**2 <= B:
				#print j,j**2
				count+=1
	line = "Case #%d: %d\n"%(i+1,count)
	of.write(line)