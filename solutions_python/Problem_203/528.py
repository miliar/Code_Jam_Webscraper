def test():
	R,c = map(int,raw_input().split(' '))
	ca = [raw_input() for _ in xrange(R)]
	while '?'*c in ca:
		i = ca.index('?'*c)
		if i>0:
			ca[i]=ca[i-1]
		else:
			j=i+1
			while '?'*c == ca[j]:
				j+=1
			ca[i]=ca[j]
	for z in ca:
		temp = list(z)
		while '?' in temp:
			i = temp.index('?')
			if i>0:
				temp[i]=temp[i-1]
			else:
				j=i+1
				while temp[j] == '?':
					j+=1
				temp[i]=temp[j]
		print "".join(temp)



N = input()
for i in xrange(N):
	print "Case #"+str(i+1)+":"
	test()
