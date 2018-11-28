f=open('candy_small.in','r')
cases= f.readline()
for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":",
	num = f.readline()
	num = int(num)
	array = f.readline()
        for j in range(0,num):
		list = array.split(" ")
		intarray = [int(x) for x in list]
		xorsum=0
		sum=0
		for k in intarray:
			xorsum=xorsum^k
			sum=sum+k
	if xorsum==0:
		intarray.sort()
		print sum-intarray[0] 
	else:
		print "NO"



