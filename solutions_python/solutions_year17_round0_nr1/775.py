def solve(pancakes, k):
	pancakes = [pancake == '+' for pancake in pancakes]
	flips = 0
	for i in range(len(pancakes)-k+1):
		if not pancakes[i]:
			flip(pancakes, k, i)
			flips += 1
	for i in range(len(pancakes)-k+1, len(pancakes)):
		if not pancakes[i]:
			return 'IMPOSSIBLE'
	return flips

def flip(pancakes, k, i):
	for j in range(i, i+k):
		pancakes[j] = not pancakes[j]

T = int(raw_input())
for t in range(1, T+1):
	[pancakes, k] = raw_input().split()
	print("Case #{0}: {1}".format(t, solve(pancakes, int(k))))

