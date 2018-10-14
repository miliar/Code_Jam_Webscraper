f=open('goro.in','r')
cases= f.readline()
for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":",
	num = int(f.readline())
	array = f.readline().split(" ")
	numbers = [int(x) for x in array]
	count=0
	for k in range(0,num):
		if (numbers[k] != k+1 ):
			count+=1
	print str(count)+".000000"

