import sys


def solve(shy):
	now_clapping = shy[0]
	friends = 0
	for shyness in range(len(shy)-1):
		if now_clapping > shyness+1:
			now_clapping += shy[shyness+1]
		else:
			new_friends = shyness+1 - now_clapping
			now_clapping += shy[shyness+1] + new_friends
			friends += new_friends

	return friends



T = int(sys.stdin.readline().strip())


for t in range(T):
	line = sys.stdin.readline().strip()
	s = line.split(" ")
	shyness = s[1]
	shy = []
	i = 0
	for c in shyness:
		shy.append(int(c))
		i=i+1
	#print shy

	print ("Case #{0}: {1}".format(t+1, solve(shy)))

	