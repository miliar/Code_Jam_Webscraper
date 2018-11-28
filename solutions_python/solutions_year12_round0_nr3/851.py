f=open('test.txt','r')
q=open('ans.txt','w')

def getperms(a):
	z=str(a)
	ret=[]
	for i in range(1,len(z)):
		ret.append(int(z[len(z)-i:]+z[:len(z)-i]))
	return ret

for i in range(1,1+int(f.readline())):
	[a,b]=[int(j) for j in f.readline().split()]
	count=0
	s=set([])
	for j in range(a,b+1):
		for k in getperms(j):
			if k>=a and k<=b and k!=j and (str(k)+str(j)) not in s:
				count+=1
				s.add(str(k)+str(j))
				s.add(str(j)+str(k))
	print 'Case #' + str(i) + ': ' + str(count)
	q.write('Case #' + str(i) + ': ' + str(count) + '\n')
q.close()
		
