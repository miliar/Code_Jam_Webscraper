testCase=int(input())
for i in range(testCase):
	num=input()
	temp=num
	k=int(num)
	for j in range(k,0,-1):
		l=len(temp)
		for m in range(l-1,0,-1):
			if(int(temp[m])<int(temp[m-1])):
				temp=int(temp)-1
				temp=str(temp)
				break;
	print('Case #',i+1,': ',int(temp),sep='')
