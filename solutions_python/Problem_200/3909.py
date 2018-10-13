def make_tidy(n):
	dig = [int(x) for x in str(n[0])]
	#print ("In {}, len {}".format(dig,len(dig)))
	for j in range(len(dig)-1):
		if dig[j+1] < dig[j]:
			dig[j] = dig[j] - 1
			for d in range(j+1,len(dig)):
				dig[d] = 9

	for k in range(len(dig)-1):
		m = (len(dig)-1) - k 
		if dig[m-1] > dig[m]:
			dig[m] = 9
			dig[m-1] = dig[m-1] - 1

	return dig

t = int(input())
for i in range(1, t + 1):
	n = [str(s) for s in input().split(" ")]
	result = make_tidy(n)
	print("Case #{}: {}".format( i,int("".join(str(x) for x in result)) ) )
