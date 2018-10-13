for i in range(int(input())):
	n = int(input())
	if(n<10):
		print('Case #{0}: {1}'.format(i+1,n))
		continue	
	s = list(str(n))
	l = len(s)
	if(n == int("".join(sorted(str(n))))):
		print('Case #{0}: {1}'.format(i+1,n))
		continue	
	while(n != int("".join(sorted(str(n))))):
		damm = []
		for j in range(l-1):
			if(s[j]<=s[j+1]):
				damm.append(s[j])
			else:
				del damm[:]
		damm.append(s[l-1])
		num = "".join(damm)
		n = n-(int(num)+1)
		s = list(str(n))	
	print('Case #{0}: {1}'.format(i+1,n))	

