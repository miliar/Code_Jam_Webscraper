def recurse(a, b, c, sub):
	if sub>max(a,b,c):
		return 1
	
	sum=0
	sum+=recurse(a,b,c,2*sub)
	if a>=sub:
		sum+=recurse(a-sub,b,c,2*sub)
	if b>=sub:
		sum+=recurse(a,b-sub,c,2*sub)
	if min(a,b,c)>=sub:
		sum+=recurse(a-sub,b-sub,c-sub,2*sub)
	return sum

nR=int(input())
for run in range(nR):
	data=input().split()
	print("Case #"+str(run+1)+": "+str(recurse(int(data[0])-1, int(data[1])-1, int(data[2])-1, 1)))