
def bath(a,b):
	count = 0
	d = 0
	c = 1/2
	while b>0:
		d += c
		c *= 2
		b = b//2
		count += 1
	return int(d),c
		

for i in range(1,int(input())+1):
	N,K = map(int,input().split())
	de, num= bath(N,K)
	lis = [(N-de)//int(num)]*int(num)
	sumi = sum(lis)
	df = N-de-sumi
	for j in range(int(df)):
		lis[j] += 1
	v = lis[int(K-num)]
	if v != 0:
		a = int((v-1)//2)
		b = int(v//2)
	else:
		a,b =0,0		 
	print("Case #{}: {} {}".format(i,max(a,b),min(a,b)))
	