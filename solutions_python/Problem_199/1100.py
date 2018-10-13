def change(s,p,k):
	for i in range(p,p+k):
		if s[i]:
			s[i]=0
		else:
			s[i]=1

def do(lst,k):
	t=0
	for i in range(len(lst)-k+1):
		if not lst[i]:
			t+=1
			change(lst,i,k)
	return t

def magic(s,k):
	lst=[]
	for i in s:
		if i=="-":
			lst.append(0)
		else:
			lst.append(1)
	t=do(lst,k)
	for i in lst[-k-1:]:
		if not i:
			return "IMPOSSIBLE"
	return t

file=open("/home/yuxh/Desktop/a/A.in")
T=int(file.readline()[:-1])
for i in range(T):
	[s,k]=file.readline()[:-1].split()
	k=int(k)
	ans=magic(s,k)
	print("Case #"+str(i+1)+": "+str(ans))
