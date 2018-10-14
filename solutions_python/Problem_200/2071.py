z = []
for a in range(int(input())):
	x = int(input())
	for i in range(x,0,-1):
		k = str(i)
		if k[-1]!=0 and all(k[b] <= k[b+1] for b in range(len(k)-1)):
			z.append(i)
			break
for c,i in enumerate(z): print("Case #" + str(c+1) + ":", i)
