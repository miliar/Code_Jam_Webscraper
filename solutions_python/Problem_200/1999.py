t2=int(input())


arr2=[]



while t2>0:
		n=int(input())
		arr2.append(n)
		t2-=1
for p in range(len(arr2)):
	flg=0




	if arr2[p]<10:
		num=arr2[p]
	elif arr2[p]==10:
		num=9
	
	else:
		m=arr2[p]
		while flg!=1:
			
			l=str(m)
			li=list(str(m))
			
			for i in range(len(li)-1):
				if int(li[i])>int(li[i+1]):
					ind=i
					flg=0
					break
				else:
					flg=1
				
			if flg==0:
				strng=''
				for k in range(i):
					strng=strng+str(li[k])
				no=int(li[i])-1
				strng=strng+str(no)
				
				for k in range(len(strng),len(li)):
					strng=strng+'9'
				num=int(strng)
				m=num
			else:
				num=m
		
	strng="Case #"+str((p+1))+": "+str(num)
	print(strng)
			

