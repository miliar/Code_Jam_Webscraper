def bathroomFast(n, k):
	if n == k:
		return 0, 0
	elif k == 1:
		if isOdd(n):
			return ((n-1)//2, (n-1)//2)
		else:
			return ((n//2), (n//2) - 1)
	else:
		if isOdd(n) and isOdd(k):
			return bathroomFast((n-1)//2, k//2)
		elif isOdd(n) and not isOdd(k):
			return bathroomFast((n-1)//2, ((k-1)//2) + 1)
		elif not isOdd(n) and isOdd(k):
			return bathroomFast(n//2 - 1, k//2)
		else:
			return bathroomFast(n//2, (k//2))

def isOdd(n):
	return n % 2 == 1

t = int(input())
for i in range(1, t+1):
	n, k = input().split(" ")
	n, k = int(n), int(k)
	answer1, answer2 = bathroomFast(n, k)
	print("Case #{}: {} {}".format(i, answer1, answer2))
	