t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	n_str = str(n)
	l=[]
	for temp in range(len(n_str)):
		l.append(int(n_str[temp]))
	for k in range(len(l)-1, 0, -1):
		if(int(l[k]) >= int(l[k-1])):
			continue
		else:
			l[k-1] -= 1
			for j in range(k,len(l)):
				l[j] = 9
	s = map(str, l)
	s = ''.join(s)
	s=int(s)
	print "Case #{}: {}".format(i+1, s)

