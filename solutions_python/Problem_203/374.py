def test():
	r,c = map(int,raw_input().split(' '))
	cake = [raw_input() for _ in xrange(r)]
	while '?'*c in cake:
		i = cake.index('?'*c)
		if i>0:
			cake[i]=cake[i-1]
		else:
			j=i+1
			while '?'*c == cake[j]:
				j+=1
			cake[i]=cake[j]
	for w in cake:
		t = list(w)
		while '?' in t:
			i = t.index('?')
			if i>0:
				t[i]=t[i-1]
			else:
				j=i+1
				while t[j] == '?':
					j+=1
				t[i]=t[j]
		print "".join(t)



T = input()
for i in xrange(T):
	print "Case #"+str(i+1)+":"
	test()