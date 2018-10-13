import math
t = long(raw_input())
for i in range(t):
	count = 0
	ip = raw_input()
	l = ip.split()
	a = long(l[0])
	b = long(l[1])
	for j in range(a,b+1):
		s = str(j)
		k = 0
		l = len(s)-1		
		while(k-l<=0):
			if s[k] == s[l]:
				k += 1
				l -= 1
				flag = 1
			else:
				flag =0
				break
		if flag == 1:	
			s1 = math.sqrt(j)
			if s1 == int(s1):
				s1 = str(int(s1))
				k = 0
				l = len(s1)-1		
				while(k-l<=0):
					if s1[k] == s1[l]:
						k += 1
						l -= 1
						flag1 = 1
					else:
						flag1 =0
						break
				if flag1 == 1:
						count += 1
	print "Case #%i: %i"%(i+1,count)
