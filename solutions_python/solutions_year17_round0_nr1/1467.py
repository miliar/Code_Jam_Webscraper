def flip(pancakes):
	d = {'+':'-', '-':'+'}
	return "".join([d[x] for x in pancakes])

t = int(input())
for tc in range(t):
	pancakes, k = [x for x in input().split()]
	k = int(k)
	c = 0
	for i in range(len(pancakes) - k + 1):
		if pancakes[i] == '-':
			pancakes = pancakes[:i] + flip(pancakes[i:i+k]) + pancakes[i+k:]
			c += 1
	if '-' in pancakes:
		print ("Case #{0}: IMPOSSIBLE".format(tc + 1))
	else:
		print ("Case #{0}: {1}".format(tc + 1,c))