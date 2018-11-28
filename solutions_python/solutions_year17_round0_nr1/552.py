myout=open("myout.txt","a")
with open('input2.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
t=int(inp[0])
for ind in range(1,t+1):
	arr=[]
	arr1=inp[ind]
	for l in range(len(arr1)):
		if arr1[l]=="-" or arr1[l]=="+":
			arr.append(arr1[l])
			y=l
	y+=1
	num=[]
	for z in range(y,len(arr1)):
		num.append(arr1[z])
	k=int(''.join(str(i) for i in num))
	n=len(arr)
	count=0
	flag=0#if flag is -1 then break
	for i in range(n):
		if arr[i]=="-":
			r=i
			flag=0
			count+=1
			if k+r>n:
				flag=-1
				break
		else:
			flag=1
		if flag==0:	
			for j in range(r,k+r):
				if arr[j]=="-":
					arr[j]="+"
				else:
					arr[j]="-"
	
	if flag==-1:
		myout.write("Case #"+str(ind)+": IMPOSSIBLE"+"\n")
	else:
		myout.write("Case #"+str(ind)+": "+str(count)+"\n")

