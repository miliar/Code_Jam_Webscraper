n=input()
n=int(n)
inarr=[]
for i in range (0,n):
	f=input()
	inarr.append(f)



def tidynos(a,j):
	leng=len(a)
	no=int(a)
	arr=list(a)
	sarr=sorted(arr)
	if(sarr== arr) :
		print("Case #%d: %s"%(j+1,a))
	else:
		x=arr.index(max(arr))
		if(x==leng-1):
			
			arr[0]=str(int(arr[0])-1)
			for i in range(1,leng):
				arr[i]=str(9)
			if(arr[0]=='0'):
				arr=arr[1:]
			st="".join(arr)

		else:	
			arr[x]=str(int(arr[x])-1)
			for i in range(x+1,leng):
				arr[i]=str(9)
			if(arr[0]=='0'):
				arr=arr[1:]
			st="".join(arr)
			
		print("Case #%d: %s"%(j+1,st))

for i in range (0,n):
	
	tidynos(inarr[i],i);
