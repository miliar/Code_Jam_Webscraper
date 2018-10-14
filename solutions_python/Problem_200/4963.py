t=int(input())
arr=[]
while t>0:
		n=int(input())
		arr.append(n)
		t-=1
print("\n\n\n")
for p in range(len(arr)):
	flg=0
	if arr[p]<10:
		num=arr[p]
	else:
		m=arr[p]
		while flg!=1:
			l=str(m)
			li=list(str(m))
			for i in range(len(li)-1):
				if int(li[i])<=int(li[i+1]):
					flg=1
				else:
					flg=0
					flg2=0
					for j in range(i+1,len(li)-1):
						if int(li[j])==int(li[j+1]):
							flg2=0
						else:
							flg2=1
							break
					ind=i+1
					break
			if flg==0:
				if flg2!=0:
					cn=len(li[ind:])-1
					m=m-1
				else:
					m-=1

			else:
				num=m
	strng="Case #"+str((p+1))+": "+str(num)
	print(strng)
			

