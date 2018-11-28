import math
T = int(input())

for r in range(1, T+1):
	N, K = map(int, input().split())
	empty = {N: 1}
	result = (0, 0)
	while K > 0:
		chosen = max(empty.keys())

		i, j = math.ceil((chosen-1)/2), math.floor((chosen-1)/2)
		if i not in empty:
			empty[i] = 0
		if j not in empty:
			empty[j] = 0
		empty[i] += empty[chosen]
		empty[j] += empty[chosen]
		K -= empty[chosen]
		del empty[chosen]
		result = (i, j)
	result = ' '.join(map(str, result))
	print(f"Case #{r}: {result}")
