myout2=open("myout2.txt","a")
with open('input.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
t=int(inp[0])

for ind in range(1,t+1):
	arr=[]
	n=len(inp[ind])
	for i in range(n):
		arr.append(int(inp[ind][i]))
	i=n-1
	flag=1
	while flag:
		while arr[i]>=arr[i-1] and i>0:
			i-=1
		if i!=0:
			arr[i-1]-=1
		else:
			flag=0
		j=i
		if i!=0:
			for k in range(j,n):
				arr[k]=9
	for i in range(n):
		if arr[i]!=0:
			break
	y="".join(str(x) for x in arr[i:])
	myout2.write("Case #"+str(ind)+": "+y+"\n")
		
