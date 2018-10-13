inp=open('D-large.in','r')
out=open('D-large.out','w')
cases= inp.readline()
for i in range(1,int(cases)+1):
	out.write("Case #"+str(i)+": ")
	num = int(inp.readline())
	numbers = [int(x) for x in inp.readline().split(" ")]
	count=0
	for k in range(0,num):
		if (numbers[k] != k+1 ):
			count+=1
	out.write(str(count)+".000000\n")
inp.close()
out.close()