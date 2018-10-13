from sys import stdin as cin,stdout as cout

for t in range( int(cin.readline())):
	a,b,k = map(int,cin.readline().split())
	d=[]
	for i in range(a):
		for j in range(b):
			if i&j < k:
				d.append((i,j))
	m = len(list(set(d)))
	cout.write('Case #'+str(t+1)+': '+str(m)+'\n')




