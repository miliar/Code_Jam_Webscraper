import sys
fp  =open('input','r')
#data = sys.stdin.readlines();
data  = fp.readline()
T = int(data.split(' ')[0]);
#print data
j = 0
while(T):
	T= T-1
	j = j+1
	dp = fp.readline();
	vp = dp.split(' ')
	A = vp[0]
	B = vp[1]
	count = 0
	a = int(A)
	b = int(B)
	l1 = len(str(a))
	l2 = l1+l1
	while (a < b):
		st = str(a);
		stp = st+st;
		lst = [st]
		for i in range(0,l1):
			if stp[i:i+l1]>st and stp[i:i+l1]<=B and stp[i:i+l1] not in lst:
				count = count +1
				lst.append(stp[i:i+l1])
		a = a+1
	print "Case #"+str(j)+": "+str(count)		
