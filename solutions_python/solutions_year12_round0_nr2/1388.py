t= input()
for i in range(t):
	s1 = raw_input().split()
	n = int(s1[0])
	s = int(s1[1])
	p = int(s1[2])
	vals = [int(v) for v in s1[3:]]
	vals.sort(reverse=True)
	ans = 0
	for j in range(len(vals)):
		temp = (vals[j]-p)/2
		if temp >= p:
			ans+=1
			continue
		if temp < 0 : continue
		if p-temp > 2: break
		elif p-temp == 2: 
			if s<=0: break
			s-=1
			ans+=1
		else:
			ans+=1
	print "Case #"+str(i+1)+":",ans
