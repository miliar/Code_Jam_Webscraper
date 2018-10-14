cases  = int(input())
i=0

while(i<cases):
	count=0
	S,K = input().split(" ")
	K = int(K)
	l = list(S)
	j=0
	while(j<len(l)):
		if (not (l.__contains__("-"))):
			print("Case #"+str(i+1)+": "+str(count))
			break
		if (K > len(l)):
			print("Case #"+str(i+1)+": IMPOSSIBLE")
			break
		if (l[j] == "-"):
			if (j+K-1 < len(l)):
				m=j+K-1
				n=j
				while(n<=m):
					if(l[n] == "+"):
						l[n] = "-"
					else :
						l[n] = "+"
					n+=1
				count+=1
		j+=1
	if(l.__contains__("-")):
		print("Case #"+str(i+1)+": IMPOSSIBLE")
		
	i+=1