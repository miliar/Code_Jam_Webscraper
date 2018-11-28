
def chk(arr):
	s=len(arr)
	for j in range(s-1):
		if(arr[j]>arr[j+1]):
			arr[j+1:]=[0]*len(arr[j+1:])
			break
def validate(arr):
	for i in range(0,len(arr)-1):
		if(arr[i]>arr[i+1]):
			return False
	return True

x=int(input())
y=1
for i in range(x):
	n=int(input())
	dig = list(int(d) for d in str(n))
	l=len(dig)
	if(validate(dig)):
		print(r"Case #"+str(y)+": " +str(int(''.join(map(str,dig)))))
		y=y+1
	elif(all(p == 1 or p == 0 for p in dig)):
		print(r"Case #"+str(y)+": " +'9'*(l-1))
		y=y+1
	elif(l==1):
		print(r"Case #"+str(y)+": " + str(n))
		y=y+1
	elif(len(set(dig))==1):
		print(r"Case #"+str(y)+": " + str(n))
		y=y+1
	elif(n<int(str(dig[0])*len(dig))):
		print(r"Case #"+str(y)+": " +str(dig[0]-1)+'9'*(l-1))
		y=y+1
	else:
		chk(dig)
		print(r"Case #"+str(y)+": " +str(int(''.join(map(str,dig)))-1))
		y=y+1
