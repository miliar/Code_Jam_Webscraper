PI = 3.14159265359
number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	return map(int, stripped_example.split(" "))

def solve(N, K, pancakes):
	o_pancakes = sorted(pancakes, key = lambda x:x[0])
	lateral = [0]*N
	top = [0]*N
	for pancake in range(N):
		lateral[pancake] = 2 * o_pancakes[pancake][0] * o_pancakes[pancake][1]
		top[pancake] = o_pancakes[pancake][0] * o_pancakes[pancake][0]
	m = 0
	for p in range(K - 1,N):
		height = lateral[p]
		if p > 0:
			height += sum(list(reversed(sorted(lateral[:p])))[:K -1])
		m = max(m, height + top[p])

	return str(m*PI)



for n in xrange(int(number)):
	example = raw_input()
	(N, K) = parseInput(example)
	pancakes = []
	for i in range(N):
		(R, H) = parseInput(raw_input())
		pancakes.append((R, H))
	print "Case #" + str(n + 1) +": " + solve(N,K,pancakes)