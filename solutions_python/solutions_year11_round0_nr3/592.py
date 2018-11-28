f=open('candy.in','r')
cases= f.readline()


for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":",
	num = int(f.readline())
	array = f.readline().split(" ")
	intarray = [int(x) for x in array]


	flag=0
	for k in intarray:
		flag=flag^k
	if flag==0:
		sum=0
		for k in intarray:
			sum=sum+k
		print sum-min(intarray)
	else:
		print "NO"


