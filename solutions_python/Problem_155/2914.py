inp = open("A-large.in","r")
output = open("out1.txt","a")

m = inp.readline()

for i in range(int(m)):
	st = inp.readline()
#	l = [i for i in raw_input().split()]
	l = [j for j in st.split()]
	k = int(l[0])
	num = l[1]
	lis = [int(j) for j in num]
	foo = lis[0]
	s = 0
	for j in range(1,len(lis)):
#		print "inside: ",foo,i,lis[i],s
		if foo < j and lis[j]!=0:
			s += j-foo
			foo += j-foo+lis[j]
		else:
			foo += lis[j]
#		print "outside: ",foo,i,lis[i],s
	output.write("Case #" + str(i+1) + ": " + str(s))
	output.write('\n')
