f=open('C-large.in','r')
out=open('C-large.out','w')
cases= f.readline()

for i in range(1,int(cases)+1):
	out.write("Case #"+str(i)+": ")
	f.readline()
	input = [int(x) for x in f.readline().split(" ")]
	if reduce(lambda x,y:x^y, input) == 0:
		out.write(str(sum(input) - min(input))+'\n')
	else:
		out.write("NO\n")
f.close()
out.close()