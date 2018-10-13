f=open('A-large.in','r')
n=int(f.readline())
t=1
o=open("res","w+")
while t<=n:
	
	l=f.readline().split()
	m=int(l[0])
	k=0
	l=l[1]
	u=0
	for i in range(len(l)):
		if k==m:
			break
		else:
			j=int(l[i])
			if j==0 and u<=i:
				k+=1
				u+=1
			else:
				u+=j

	# print k
	print >> o , "Case #"+str(t)+": "+str(k)
	t+=1

o.close()
f.close()