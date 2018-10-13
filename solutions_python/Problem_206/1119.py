t=int(input())
for i in range(t):
	D,N = map(int,input().split(" "))
	l=[];
	for j in range(N):
		K,S = map(int,input().split(" "))
		dis = D-K
		time = dis/S
		l.append(time)
	ma=max(l)
	print("Case #"+str(i+1)+":",end=" ")
	print('{0:.6f}'.format(D/ma))

