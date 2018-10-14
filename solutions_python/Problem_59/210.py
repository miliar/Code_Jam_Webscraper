import sys

Dir={};

def addnew( tocreate ):
#	print "To create:",tocreate
	count=0
	rootd=Dir;
	for p in tocreate:
	#	print "dir to add:",p;
		if( p in rootd ):
			rootd=rootd[p]
		else:
			rootd[p]={};
			rootd=rootd[p];
	#		print "Adding....",p
			count=count+1;
	return count
		


f=open(sys.argv[1],'r')
l=f.readline()
cases=int(l)
#print cases;



for m in range(1,cases+1):
	Dir={}
	print "Case #"+str(m)+":",;
	inputline = f.readline();
	nums=inputline.rstrip().split(' ')
	#print "inputline:",inputline; #nums[0]
	#print "nums",nums;

	numpresent=int(nums[0]);
	numadd=int(nums[1]);
	#print numpresent,numadd;

	for i in range(1,1+numpresent):
		inputline = f.readline();
		inputline=inputline.rstrip().split('/')
	#	print inputline
		c=addnew(inputline[1:]);
	#	print c

	
	k=0;
	for i in range(1,1+numadd):
		inputline = f.readline();
		inputline=inputline.rstrip().split('/')
		c=addnew(inputline[1:]);
		k=k+c;
	#	print c
	#	print inputline

	print k

f.close()

