def f(a):
	a=str(a)
	b=a[::-1]
	if a==b:
		return 1
	else:
		return 0

ans=[]
val=10000001
for i in range(val):

	if f(i)==1 and f(i*i)==1:
		ans.append(i*i)
	
#print len(ans)
#print ans
a=input()
ctr=1
while a:
	b=raw_input()
	b=b.split(' ')
	st=(int)(b[0])
	en=(int)(b[1])
	fin=0
	for i in range(1,len(ans)):
		if ans[i]<=en and ans[i]>=st:
			fin+=1
		elif ans[i]>en:
			break
	print "Case #"+(str)(ctr)+": "+(str)(fin)
	ctr+=1
	a=a-1
	

