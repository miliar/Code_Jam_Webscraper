import copy
N=int(input())
for I in range(N):
	temp=input().split()
	R=int(temp[0])
	C=int(temp[1])
	data=[[j for j in input()] for i in range(R)]
	for i in range(R):
		for j in range(C):
			k=0
			if data[i][j]=="?":
				while j+k<C and data[i][j+k]=="?":
					k+=1
				if j+k<C:
					data[i][j]=data[i][j+k]
				else:
					k=0
					while j-k>=0 and data[i][j-k]=="?":
						k+=1
					if j-k>=0:
						data[i][j]=data[i][j-k]
	
	if "?" in data[0]:
		k=0
		while "?" in data[k]:
			k+=1
		data[0]=copy.deepcopy(data[k])
	for i in range(1,R):
		if "?" in data[i]:
			data[i]=copy.deepcopy(data[i-1])
	
	print("Case #"+str(I+1)+":")
	for i in range(R):
		ans=""
		for j in data[i]:
			ans=ans+j
		print(ans)