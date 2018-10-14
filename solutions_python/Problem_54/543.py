def gcd(a,b):
	if(b==0):
		return a;
	else:
		return gcd(b,a%b);

testcases = input()
i=0
while(i<testcases):
	a = raw_input()
	a = a.split(' ')
	size = int(a[0])
	j=1
	val = []
	while j <= size:
		val.append(int(a[j]))
		j=j+1
	val.sort()
	j=1
	t=0
	while j <= size:
		k=j
		while k < size:
			t=gcd(t,val[k]-val[j-1])
			k=k+1
		j=j+1
	x=val[0]%t;
	if(val[0]%t):
		x = t-x;		
	print "Case #"+str(i+1)+": "+str(x);
	i=i+1;
