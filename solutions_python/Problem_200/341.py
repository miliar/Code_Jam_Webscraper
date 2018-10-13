t = int(input())

for ii in range(t):
	num = [-1 for i in range(20)]
	x = int(input())
	y = x

	i = 19
	while(x>0):
		num[i] = x%10
		x = x//10
		i-=1
	#print(num)

	i = 18
	while(num[i]!= -1):
		if(num[i] > num[i+1]):
			num[i]-=1
			for j in range(i+1,20):
				num[j] = 9
		i-=1

	ans = 0
	for i in range(20):
		if(num[i] != -1):
			ans*= 10
			ans+=num[i]

	

	print("Case #",ii+1,": ",ans,sep="")





