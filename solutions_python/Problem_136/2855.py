num_of_testcases = int(raw_input())
k = 2.0000000
times = []
for num_line in range(num_of_testcases):
	all_data = []
	line = raw_input()
	data = map(float,line.split())
	c = data[0]
	f = data[1]
	x = data[2]
	datas= []
	datas.append(x/k)
	a = k
	res = c/k
	n = 0
	chk = True
	while chk :
		#j = 0
		n += 1.0000000
		if (n == 1.0000000) :
			#print res
			#print "{0}".format(k+f)
			res = res + (x/(k+f))
			datas.append(res)
			#print datas
		elif (n > 1.0000000):
			res = res + (-x/(k+(n-1.0000000)*f))+ (c/(k+(n-1.0000000)*f)) + x/(k+(n*f))
			datas.append(res)
			#print datas
		#print "data {0} : {1}".format(int(n)-1,datas[int(n)-1])
		#print "data {0} : {1}".format(int(n),datas[int(n)])
		if (datas[int(n)-1] < datas[int(n)]):
			break
	datas.sort()
	times.append(datas[0])
num = 1
for time in times :
	print "Case #{0}: {1:.7f}".format(num,time)
	num += 1