t = int(input())

for ii in range(t):
	d,n = map(int, input().split())
	times = []

	for i in range(n):
		st, sp = map(int, input().split())

		times.append((d-st)/sp)

	ans = d/max(times)

	print("Case #",ii+1,": ","%.6f" %ans,sep="")
