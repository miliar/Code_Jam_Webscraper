

def f(x):
	if x%2 == 1:
		return (x-1)//2,(x-1)//2
	else:
		return x//2,x//2-1

N = int(input())

for i in range(N):


	dic = {}
	n, k = [int(i) for i in input().split()]
	max_ref = n
	dic[n] = 1

	while k > dic[max_ref]:
		k -= dic[max_ref]
		x, y = f(max_ref)
		if x in dic:
			dic[x] += dic[max_ref]
		else:
			dic[x] = dic[max_ref]
		if y in dic:
			dic[y] += dic[max_ref]
		else:
			dic[y] = dic[max_ref]
		del dic[max_ref]
		max_ref = max(dic.keys())

	print('Case #'+str(i+1)+': '+' '.join([str(i) for i in f(max_ref)]))

	
