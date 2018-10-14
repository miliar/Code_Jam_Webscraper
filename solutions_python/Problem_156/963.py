def countTime(h, p):
	moves = 0
	for x in p:
		moves += (x-1) / h;
	return moves + h

def solve(n, p):
	res = max(sum(p), max(p))
	for h in range(1, max(p)+1):
		res = min(res, countTime(h, p))
	return res

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		n = int(raw_input())
		print("Case #{0}: {1}".format(i, solve(n, map(int, raw_input().split(' ')))));

if __name__ == '__main__':
	main()