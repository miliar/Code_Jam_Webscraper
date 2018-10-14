file_write=open("standing_output.txt","w+")
file_read=open("A-large.in","r")
noOfTestCases=int(file_read.readline())
for i in range(1,noOfTestCases+1):
	line = file_read.readline()
	s_max,s_digits = line.split()
	digits_list = list(int(d) for d in str(s_digits))
	invites=0
	claps=digits_list[0]
	j=1
	while(j<int(s_max)+1):
		if(claps>=j):
			claps=claps+digits_list[j]
			j=j+1
		else:
			claps=claps+1
			invites=invites+1
	file_write.write("Case #%d: %s\n"%(i,invites))