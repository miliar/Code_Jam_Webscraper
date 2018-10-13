
def stall(a,b):
	count = 0
	defe = 0
	c = 1/2
	while b>0:
		defe += c
		c *= 2
		b = b//2
		count += 1
	return defe//1,c,count
		

for i in range(1,int(input())+1):
	n,k = map(int,input().split())
	de, num,cou= stall(n,k)
	ar = [(n-de)//int(num)]*int(num)
	su = sum(ar)
	d = n-de-su
	for j in range(int(d)):
		ar[j] += 1
	m = ar[int(k-num)]
	if m != 0:
		a = int((m-1)//2)
		b = int(m//2)
	else:
		a,b =0,0		 
	print("Case #{}: {} {}".format(i,max(a,b),min(a,b)))
	
	