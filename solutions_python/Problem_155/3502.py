a = raw_input("Input File - \n")
b = raw_input("Output File - \n")
inp = open(a)
out = open(b ,'w')
out.truncate()
itr = int(inp.readline())
for i in xrange(itr):
	smax , c = inp.readline().split()
	smax = int(smax)
	c = list(c)
	c = [int(s) for s in c]
	sum = 0
	d = 0
	for j in xrange(smax+1):
		print "jskjfdj"+str(d)
		if j==0:
			d = d + c[j]
		elif j>0 and c[j]>0:
			print j ,d
			if d>=j:
				d = d + c[j]
				print d
			else :
				sum = sum + (j - d )
				print j , d
				print sum
				d = d + c[j] + sum
	print "\n\n\n\n"
	out.write("Case #"+str(i+1)+": "+str(sum)+"\n")
inp.close()
out.close()