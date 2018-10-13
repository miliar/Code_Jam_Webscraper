f=open('test.txt','r')
g=open('test2.txt','r')
s=open('ans.txt','w')
d={}
q=set([])
for i in range(1,1+int(f.readline())):
	s1=f.readline().strip()
	s2=g.readline().strip()
	s2=s2[9:]
	for j in range(len(s1)):
		if s1[j]!=' ':
			d[s1[j]]=s2[j]
			q.add(s2)
d['z']='q'
for i in range(97,123):
	if not chr(i) in d:
		print chr(i)
		w1=chr(i)
	if not chr(i) in q:
		w2=chr(i)
d[w1]=w2
print len(d)

c=open('test3.txt','r')
for i in range(1,1+int(c.readline())):
	s1=c.readline().strip()
	ans=''
	for j in s1:
		if j==' ':
			ans+=' '
		else:
			ans+=d[j]
	print 'Case #' + str(i) + ': ' + ans
	s.write('Case #' + str(i) + ': ' + ans +'\n')
s.close()

	