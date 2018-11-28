N = 0
ans = 0
X = 0
dig = []

def solve(idx, n, last, tight):
	global ans
	if (n <= N):
		ans = max(ans, n)
	elif (idx == X):
		return
	go = n
	for i in range(idx, X):
		go = go*10 + 9
	if (go <= N and go <= ans):
		return 
	if (tight):
		for i in range(dig[idx], -1, -1):
			if (i >= 0 and i >= last):
				solve(idx+1, n*10 + i, i, i == dig[idx])
	else:
		for i in range(9, -1, -1):
			if (i >= 0 and i >= last):
				solve(idx+1, n*10 + i, i, tight)

if __name__ == "__main__":
	t = int(input())
	for T in range(1, t+1):
		print("Case #", end="")
		print(T, end="")
		print(": ", end="")
		N = int(input())
		ans = 1
		n = N
		X = 0
		dig = []
		while(n > 0):
			dig.append(n % 10)
			n //= 10
		X = len(dig)
		dig.reverse()
		for i in range(0, dig[0]+1):
			solve(1, i, i, i == dig[0])
		print(ans)
