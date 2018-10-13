d={}
d[1]=(11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44)
d[2]=(12,14,21,22,23,24,32,34,41,42,43,44)
d[3]=(23,32,33,34,43)
d[4]=(34,43,44)
t=int(input())
for m in range(1,t+1):
	x,r,c=map(int, input().split())
	if (r*10+c) in d[x]:
		res = "GABRIEL"
	else:
		res = "RICHARD"
	print("Case #{0}: {1}".format(m,res))
