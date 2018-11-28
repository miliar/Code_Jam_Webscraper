from collections import Counter
import itertools
t = int(input())
for i in range(1, t + 1):
	nums = input().split(" ")
	n = int(nums[0])
	p = int(nums[1])
	R = [int(item) for item in input().split(" ")]
	result = [[] for _ in range(n)] 
	for j in range(n):
		packages = [int(item) for item in input().split(" ")]
		for k in range(p):
			temp = set()
			count = R[j]
			index = 1
			while 0.9 * count <= packages[k]: 
				if 0.9 * count <= packages[k] and packages[k] <= 1.1 * count:
					temp.add(index)
				index = index + 1
				count = count + R[j]
			if temp:
				result[j].append(temp)
	if n == 1:
		print("Case #{}: {}".format(i, len(result[0])))
	else:
		m1 = len(result[0])
		n1 = len(result[1])
		matrix = [[0 for _ in range(n1)] for _ in range(m1)]
		for dd in range(m1):
			for j in range(n1):
				if result[0][dd] & result[1][j]:
					matrix[dd][j] = 1
		ans = 0
		if m1 <= n1:
			for perm in itertools.permutations([i for i in range(n1)]):
				temp = sum(matrix[i][perm[i]] for i in range(m1))
				ans = max(ans, temp)
		else:
			for perm in itertools.permutations([i for i in range(m1)]):
				temp = sum(matrix[perm[i]][i] for i in range(n1))
				ans = max(ans, temp)
		print("Case #{}: {}".format(i, ans))