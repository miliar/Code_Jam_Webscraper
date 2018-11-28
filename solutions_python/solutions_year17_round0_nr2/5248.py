a=int(raw_input())
ans=[]
for i in range(a):
	last=0
	temp=raw_input()
	n=int(temp)
	while n>0:
		num=[]
		for ii in str(n):
			num.append(int(ii))
		if sorted(num)==num:
			last=int(n)
			break
		else:
			n-=1
	ans.append(last)
for i in range(len(ans)):
	print "Case #"+str(i+1)+":",ans[i]