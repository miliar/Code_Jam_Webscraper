f=open('goro_small.in','r')
cases= f.readline()
for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":",
	num = f.readline()
	num = int(num)
	array = f.readline()
	list = array.split(" ")
	intarray = [int(x) for x in list]
	count=0
	for k in range(0,num):
		if (intarray[k] != k+1 ):
			count = count + 1
	print str(count)+".000000"



