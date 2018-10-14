x=input()
def c(j):
	r=0
	t = j;
	while t != 0:
		r *= 10
		r +=t % 10
		t /= 10
	if j==r:
		return 1
	else:
		return 0
def sqrt(x):
	a= 0
	if x>=0:
		while a*a < x:
	 		a = a + 1
	 	if a*a == x:
	 	   	return a
	 	else:
	 	    	return 0
	return 0
for i in range(x):
	y=raw_input()
	y=y.split(' ')
	w=int(y[0])
	z=int(y[1])
	sum=0
	for j in range(w,z+1):
		if c(j)==1 and sqrt(j) >0 and c(sqrt(j))==1:
			sum+=1
	print 'Case #'+str(i+1)+': '+str(sum)
