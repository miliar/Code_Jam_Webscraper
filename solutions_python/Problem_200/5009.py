def genNum(n):
	num = str(n)
	arr = []
	for i in num:
		arr.append(i)
	#print(arr)
	lent = len(arr)
	isTidy = True
	for x in range(lent-1):
		if(x==lent):
			break
		elif(int(arr[x])> int(arr[x+1])):
			isTidy = False
			break
		else:
			continue
	return(isTidy)
def check(n):
	defa = genNum(n)
	cur = n
	while(not defa):
		cur = cur - 1
		defa = genNum(cur)
	return(cur)

t = int(input(""))
for ll in range(1,t+1):
	fuu = input("")
	print("Case #{}: {}".format(ll, check(fuu)))

