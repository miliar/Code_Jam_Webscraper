import sys
fp = open('input','r')
data = fp.readline()
T= int(data.split(' ')[0]);
j=0;
while(T):
	T=T-1
	j=j+1
	dp = fp.readline();
	vp = dp.split(' ')
	N= int(vp[0])
	S =int(vp[1])
	p=int(vp[2])
	ps = vp[2]
	minp =0
	normal = 0
	if p >=2:
		minp = p+p+p-4
		normal = minp+2
	else:
		minp = p
		normal = p
	count = 0
	for i in range(0,N):
		v = int(vp[3+i])
		if v >= normal:
			count =count +1
		else:
			if v >= minp and S > 0:
				count = count+1
				S=S-1
	print "Case #"+str(j)+": "+str(count)
