# cook your code here
def gapp(arr):
	a=0
	b=0
	gap=-1
	i=0
	while i<len(arr)-1:
		if arr[i]==1:
			pos=i+1
			gp2=0
			while arr[pos]!=1:
				gp2+=1
				pos+=1
			if gap<gp2:
				gap=gp2
				a=i
				b=pos
			i=pos
		else:
			i+=1
	return(a,b)


t=int(input())
N=[]
K=[]
while t>0:
	li=input().strip().split(' ')

	N.append(int(li[0]))
	K.append(int(li[1]))
	t-=1
for i in range(len(N)):
	slots=[int(0)]*(N[i]+2)
	slots[N[i]+1]=1
	slots[0]=1
	for q in range(K[i]):
		(ind1,ind2)=gapp(slots)
		slots[(ind1+ind2)//2]=1
	ls=0
	rs=0
	for q in range((ind1+ind2)//2-1,0,-1):
		if slots[q]==0:
			ls+=1
		else:
			break
	for q in range((ind1+ind2)//2+1,len(slots)):
		if slots[q]==0:
			rs+=1
		else:
			break
	print("Case #"+str(i+1)+": "+str(max(ls,rs)),str(min(ls,rs)))