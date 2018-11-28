f = open("testcase.txt")
c = int(f.readline())
for l in xrange(c):
	d = f.readline().split(' ')
	A = int(d[0])
	B = int(d[1])
	numbers = 0
	for i in range(A,B):
		for j in range(i+1,B+1):
			if (len(str(j)) == len(str(i))) and (len(str(j)) != 1): 
				test = str(j)
				for k in xrange(len(str(i))-1):
					test = test[len(test)-1] + test[:len(test)-1]
					if test == str(i):
						numbers += 1
						break
			else:
				break
	print "Case #"+str(l+1)+": "+str(numbers)
