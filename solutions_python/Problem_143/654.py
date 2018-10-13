import sys

def sol(A, B, K):
	all_winners = []
	for a in range(0, A):
		for b in range(0, B):
			all_winners.append(a & b)
	return len([x for x in all_winners if x < K])

if __name__ == "__main__":
	cases = int(sys.stdin.readline())
	for case in range(1, cases + 1):
		A, B, K = map(int, sys.stdin.readline().split())
		ways = sol(A, B, K)
		print("Case #" + str(case) + ": " + str(ways))