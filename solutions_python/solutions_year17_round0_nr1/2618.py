for t in range(int(input())):
	s,k=input().split()
	s=[i for i in s]
	#print(s)
	k=int(k)
	count=0
	for i in range(len(s)-k+1):
		#print("i"+str(i))
		if s[i]=='-':
			for j in range(i,i+k):
				#print(j)
				if s[j]=="-":
					s[j]="+"
				else:
					s[j]="-"
			count+=1
			#print(s)
	if '-' in s:
		print("Case #"+str(t+1)+": IMPOSSIBLE")
	else:
		print("Case #"+str(t+1)+": "+str(count))