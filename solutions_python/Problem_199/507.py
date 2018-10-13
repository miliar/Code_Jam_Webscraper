import sys

def solve(case):
	s, k = sys.stdin.readline().split()
	s = list(s)
	k = int(k)
	count = 0
	for i in range(len(s)-k+1):
		if s[i] == '+':
			continue
		count += 1
		for j in range(k):
			s[i+j] = '+' if s[i+j] == '-' else '-'
	
	#~ print(sys.stderr, s)
	
	for i in range(len(s)):
		if s[i] != '+':
			break
	else:
		print("Case #{}: {}".format(case, count))
		return
	print("Case #{}: IMPOSSIBLE".format(case))

def main():
	t = int(sys.stdin.readline())
	for i in range(t):
		solve(i+1)

if __name__ == "__main__":
	main()

