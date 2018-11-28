
t=int(raw_input())
for ca in range(1,t+1):
	aa=raw_input()
	aa1 = [int(i) for i in aa.split()]
	A,B,K=aa1
	Na=[]
	Nb=[]
	for i in range(0,A):
		Na.append(i)
	for i in range(0,B):
		Nb.append(i)

	res=[]


	for i in Na:
		for j in Nb:
			temp=i&j
			if (temp<K):
				res.append(temp)

	#print len(res)
	print "Case #%i: %d" %(ca,len(res))











