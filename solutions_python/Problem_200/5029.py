t = int(input())

def isTidy(n):
	return n == int(''.join(map(str, sorted(list(str(n))))))

for i in range(1, t + 1):
	n = int(input())
	while not isTidy(n):
		n -= 1
	print("Case #{}: {}".format(i, n))