for t in range(int(raw_input())):
	n = int(raw_input())
	l=[]
	
	flag =0
	if n>10:
		for j in xrange(11,n+1):
			if j%10==0:
				continue
			else:
				n_r = str(j)
				for i in xrange(len(n_r)-1):
					if bool(n_r[i]>n_r[i+1])==True:
						flag = 0
						break
					else:
						flag = 1
				if flag == 1:
					l.append(j)
		print 'Case #{}: {}'.format(t+1,l[-1])
	else:
		print 'Case #{}: {}'.format(t+1,n)
	

