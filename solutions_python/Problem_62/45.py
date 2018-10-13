if __name__=='__main__':
	a = raw_input();
	T = eval(a);


	for qqq in range(T):
		a = raw_input();
		N = eval(a);

		a=[]
		b=[]

		for i in range(N):
			c = raw_input();
			c = c.split()
	
			a.append(eval(c[0]))
			b.append(eval(c[1]))

		counter = 0

		for i in range(N):
			pair = [a[i], b[i]]
			for j in range(i+1, N):
				if (a[i]-a[j] < 0) and (b[i]-b[j] >0):
					counter+=1
				if (a[i]-a[j] > 0) and (b[i]-b[j] <0):
					counter+=1

		print 'Case #%d: %d'% (qqq+1, counter)
