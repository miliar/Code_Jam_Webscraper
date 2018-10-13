x=input()
def check(j):
	reverse=0
	temp = j;
	while temp != 0:
		reverse *= 10
		reverse +=temp % 10
		temp /= 10
	if j==reverse:
		return 1
	else:
		return 0
def sqrt(x):
	    ans = 0
	    if x >= 0:
	 	   while ans*ans < x:
	 		   ans = ans + 1
	 	   if ans*ans == x:
	 	   	return ans
	 	   else:
	 	   	return 0
	    return 0
for i in range(x):
	y=raw_input()
	y=y.split(' ')
	a=int(y[0])
	b=int(y[1])
	sum=0
	for j in range(a,b+1):
		if check(j)==1 and sqrt(j) >0 and check(sqrt(j))==1:
			sum+=1
	print 'Case #'+str(i+1)+': '+str(sum)
