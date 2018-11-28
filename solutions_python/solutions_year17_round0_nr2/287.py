filename = 'B-large.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t ,
	N = f.readline().strip()
	if len(N) == 1:
		print N
	elif int(N) < int('1'*len(N)):
		print '9'*(len(N)-1)
	else:
		i = len(N)
		for j in range(len(N)-1):
			if int(N[j+1]) < int(N[j]):
				i = j
				break
		if i == len(N):
			print N
		else:
			print(N[:N.index(N[i])] + str(int(N[i])-1) + '9'*(len(N)-N.index(N[i])-1))
