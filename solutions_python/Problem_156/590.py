
def solve():
	n = int(input())
	a = input().split(' ')
	a = list(map(int,a))
	max_v = max(a)
	r = max_v

	for i in range(2, max_v):
		k = i
		for el in a:
			k += (el // i - 1)
			if el % i > 0:
				k+=1

		if k < r:
			r = k


	return r

t = int(input())
for i in range(t):
	r = solve()
	print("Case #%s: %s" % (i+1,r))
