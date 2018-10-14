


def recurse(string):
	counter=0
	flag=False
	
	for i in range(len(string)-1,0,-1):
		if(string[i] < string[i-1]):
			string[i-1]-=1
			counter=i-1
			flag=True
	return [counter,flag]


for i in range(int(input())):
	
	string2=input()
	string=[int(k) for k in string2]
	counter,flag=recurse(string)
	ans=""
	if(flag):
		for k in string[0:counter+1]:
			ans+=str(k)
		ans+='9'*(len(string)-counter-1)
	else:
		ans+=string2

	ans=int(ans)

	print("Case #"+str(i+1)+": "+str(ans))