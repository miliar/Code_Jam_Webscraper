import sys



f=open(sys.argv[1],'r')
l=f.readline()
cases=int(l)
#print cases;



for m in range(1,cases+1):
	sc=0
	print "Case #"+str(m)+":",;
	inputline = f.readline();
	nums=inputline.rstrip().split(' ')
	N=int(nums[0]);
	K=int(nums[1]);
	B=int(nums[2]);
	T=int(nums[3]);

	#reading N
	inputline = f.readline();
	inputline=inputline.rstrip().split(' ')
	x=[]
	for i in range(0,N):
		x.append(int(inputline[i]));
		#print x
		
	inputline = f.readline();
	inputline=inputline.rstrip().split(' ')
	v=[]
	for i in range(0,N):
		v.append(int(inputline[i]));
		#print v


	x.reverse();v.reverse();
	for i in range(0,N):
		if( (B-x[i]) <= v[i]*T ):
			K=K-1
		else:
			sc=sc+K
		if K==0:
			break;

	if K==0:
		print sc
	else:
		print "IMPOSSIBLE"
		
	

f.close()

