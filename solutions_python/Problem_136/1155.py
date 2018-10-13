T = int(raw_input())

def buy1(C, F, X, current, cost):
	return X/(current+F)+C/current+cost

for tt in range(T):
	s = map(float, raw_input().split(" "))
	C = s[0]
	F = s[1]
	X = s[2]
	current = 2.0
	cost = 0
	while X/current+cost > buy1(C, F, X, current, cost):
		cost += C/current
		current += F
	print "Case #{0}: {1}".format(str(tt+1), str(cost + X/current))
