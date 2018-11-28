number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	return map(int, stripped_example.split(" "))

def solve(D, N, horses):
	latest = -1
	for h in horses:
		destination_time = (D-h[0])/float(h[1])
		latest = max(destination_time, latest)
	return D/latest

for n in xrange(int(number)):
	example = raw_input()
	(D, N) = parseInput(example)
	horses = []
	for i in range(N):
		(K, S) = parseInput(raw_input())
		horses.append((K,S))
	print "Case #" + str(n + 1) +": " + str(solve(D, N, horses))
