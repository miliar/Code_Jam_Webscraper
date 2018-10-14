def pancakeSolver(pancakes, k):
	changes = 0
	for i in range(len(pancakes) - (k) + 1):
		if pancakes[i] == '-':
			for j in range(k):
				if pancakes[i+j] == '+':
					pancakes[i+j] = '-'
				elif pancakes[i+j] == '-':
					pancakes[i+j] = '+'
			changes += 1
	for i in pancakes:
		if i == '-':
			return 'IMPOSSIBLE'
	return changes

t = int(input())
for x in range(1, t+1):
	pancakeList = []
	pancakes, k = input().split(" ")
	for i in pancakes:
		pancakeList.append(i)
	k = int(k)
	print("Case #{}: {}".format(x, pancakeSolver(pancakeList, k)))