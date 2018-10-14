from sys import stdin

input = stdin.read().split('\n')

for t in range(int(input[0])):
	ans1 = int(input[t * 10 + 1])
	ans2 = int(input[t * 10 + 6])
	chosen = set.intersection(set(input[t * 10 + 1 + ans1].split()), set(input[t * 10 + 6 + ans2].split()))
	output = "Bad magician!" if len(chosen) > 1 else ("Volunteer cheated!" if len(chosen) == 0 else chosen.pop())

	print "Case #{0}: {1}".format(t+1, output)