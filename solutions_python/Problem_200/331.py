import sys

def solve():
	num = int(sys.stdin.readline())
	num = [int(x) for x in str(num)]
	# print(num)
	num.append(10)
	curx = 1
	ans = 0
	for i in range(len(num)-1):
		ans = ans*10 + num[i]
		safe = False
		for j in range(i+1, len(num)):
			if num[i] != num[j]:
				safe = num[j]>num[i]
				break
		if not safe:
			ans -= 1
			for j in range(i+1, len(num)-1):
				ans = ans*10 + 9
			break

	return ans

ntest = int(sys.stdin.readline())
for i in range(1, ntest+1):
	ans = solve()
	print("Case #%d: %d"%(i, ans))