def solve(layout,K):
	pancakes = [s == "+" for s in layout]
	flips = 0
	for i in range(len(pancakes)):
		if not pancakes[i]:
			for j in range(K):
				if i + j >= len(pancakes):
					return "IMPOSSIBLE"
				else:
					pancakes[i+j] = not pancakes[i+j]
			flips+=1
	return str(flips)

def printNode(num,S):
	s = ""
	for i in range(S):
		if num%2 == 0:
			s += "-"
		else:
			s += "+"
		num = num/2
	return s

if __name__ == "__main__":
	t = int(raw_input())
	for i in xrange(1, t + 1):
		n, m = [s for s in raw_input().split(" ")]
		answer = solve(n,int(m))
		print "Case #" + str(i) + ":",answer
