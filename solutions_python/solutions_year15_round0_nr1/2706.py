t=int(input())
for i in range (1,t+1):
	arr=[]
	new=[]
	st1=input()
	st=st1.split(" ")
	n=len(st[1])
	extra=0
	j=0
	while (j<n):
		arr.append(int(st[1][j]))
		j=j+1
	new.append(arr[0])
	for j in arr[1:]:
		new.append(j+new[len(new)-1])
	for j in range(0,n):
		if new[j]+extra<j+1:
			extra=j+1-new[j]
	op="Case #"+str(i)+": "+str(extra)
	print(op)
	i=i+1
