def main():
	n = int(input())
	for i in range(1, n+1):
		print("Case #%d: " % i, end="")
		solve()

def solve():
	n, k = map(int, input().split())
	budget = float(input())

	cores = sorted(map(float, input().split()))
	best = 0

	for i in range(1, len(cores)+1):
		s = cores[:i]
		start = s[:-1]
		model = s[-1]

		cost = model * len(start) - sum(start)
		if cost < budget:
			v = min(1, model + (budget-cost)/len(s))
			best = v**(len(s))
			for c in cores[i:]:
				best *= c

	other = min(1, cores[0] + budget)
	for c in cores[1:]:
		other *= c

	best = max(best, other)

	print(best)

main()