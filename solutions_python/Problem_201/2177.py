def pot2(h):
	h = h
	k = 0
	while 2**k<=h:
		k+=1
	return(2**(k-1))
	
def dif(x):
	t = int(x/2)
	if x%2==0:
		return(str(t)+" "+str(t))
	else:
		return(str(t+1)+" "+str(t))

problemas = int(input())
for problema in range(problemas):
	b, h = [int(k) for k in input().split(" ")]
	pot = pot2(h)
	t = dif((b-h)//pot)
	print("Case #"+str(problema+1)+": "+t)