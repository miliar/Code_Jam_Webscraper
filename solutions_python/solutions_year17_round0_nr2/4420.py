tst=int(input())
for tt in range(0,tst):
	n=input()
	t=list(n)
	for i in range(0,len(t)-1):
		if int(t[i+1])<int(t[i]):
			f=i
			ind=i
			while f>0:
				if int(t[f])==int(t[f-1]):
					ind=f-1
				f=f-1
			t[ind]=str(int(t[ind])-1)
			
			for k in range(ind+1,len(t)):
				t[k]='9'
	ans=''.join(t)
	print("Case #%d: %d" %(tt+1,int(ans)))