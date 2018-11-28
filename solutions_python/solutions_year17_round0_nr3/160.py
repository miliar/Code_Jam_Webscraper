def bina(x):
	return bin(x)[2:]
def solve(n,k):
	a=1
	p=0
	while(a<=k):
		a*=2
		p+=1
	p-=1
	a//=2
	m1=1
	m2=0
	larger = n
	for i in range(p):
		new_larger = larger // 2
		q1=q2=0
		if(larger % 2 == 0):
			q1 += m1
			q2 += m1
			q2 += 2*m2
		else:
			q1 += 2*m1
			q1 += m2
			q2 += m2
		larger = new_larger
		m1,m2=q1,q2
	k=k-a
	if(k<m1):
		return ans(larger)
	else:
		return ans(larger-1)

def ans(x):
	return ((x)//2,(x-1)//2)



T = int(input())
for case in range(1,T+1):
	n,k=tuple(map(int,list(input().split())))
	a = solve(n,k)
	print("Case #{}: {} {}".format(case, a[0],a[1]))
