t=int(input())
for i in range(0,t):
	string=(str(input())).split(' ')
	#print(string[1])
	sum=int(0)
	req=int(0)
	x=str(string[1])
	count=int(0)
	for v in x:
		if(count>sum):
			req+=count-sum
			sum+=int(v)+1
		else:
			sum+=int(v)
		count+=1
	print("Case #"+(str(i+1))+": "+(str(req)))