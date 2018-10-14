def gcd(m,n):
	if n==0 : return m;
	return gcd(n,m%n);
	
N = eval(raw_input());
for i in range(0,N):
	tuple = raw_input().split();
	n = eval(tuple[0])
	
	tupleX = []
	for j in range(1,tuple.__len__()):
		tupleX.append(eval(tuple[j]))
	tupleX.sort()
	#print tupleX
	k = tupleX[0]
	
	tuple1 = []
	
	
	for j in range(1,tupleX.__len__()):
		tuple1.append(tupleX[j] - k)
		#print tuple1[-1]
	k1 = tuple1[0]
	for j in range(1,tuple1.__len__()):
		k1 = gcd(k1,tuple1[j])
	if k % k1 == 0:
		_out = 0
	else:
		_out = k1 - k % k1
	print "Case #"+str(i+1)+": "+str(_out)
	
	
