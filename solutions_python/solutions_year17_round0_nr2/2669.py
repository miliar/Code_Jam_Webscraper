def prints(id, val):
	print ("Case #",id,": ",val, sep='')

def extend (arr, n):
	for i in range(0, len(arr)-1):
		if (arr[i]>arr[i+1]):
			return 0
	while (len(arr)<n):
		arr.append(9)
	cur= 1
	ret= 0
	arr.reverse()
	for i in range(0, len(arr)):
		ret= ret + arr[i]*cur
		cur= cur*10
	return ret	  			

def solve (id):
	x= int(input())
	t= []
	while (x!=0):
		t.append(x%10)
		x= x//10
	t.reverse()

	ret= 0
	for i in range(0, len(t)):
		for j in range(0, t[i]):
			u= []
			for k in range(0, i):
				u.append(t[k])
			u.append(j)
			ret= max(ret, extend(u, len(t)))	

	ret= max(ret, extend(t, len(t)))
	prints(id, ret)		



t= int(input())
for i in range(1, t+1):
	solve(i) 		 