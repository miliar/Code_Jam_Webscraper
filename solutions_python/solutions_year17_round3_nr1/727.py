import math as math
import decimal

def area(pans):
	if type(pans) is list and len(pans) > 0:
		top = pans[0]['r']
		side = 0
		for pan in pans:
			side += pan['r'] * pan['h']

		return top**2 + 2 * side

	return 0

def plate(my_pans, pans, size, index, K, N):
	# print(my_pans, pans, size, index, K, N)
	if size < K and index < N:
		my_pans_2 = my_pans + [pans[index]]
		size_2 = size + 1
		index = index + 1
		plate_1 = plate(my_pans, pans, size, index, K, N)
		plate_2 = plate(my_pans_2, pans, size_2, index, K, N)
		return max(plate_1, plate_2)
	else:
		return area(my_pans)


T = int(input())
for t in range(1, T + 1):
	N, K = [int(s) for s in input().split(" ")]
	pans = []
	for i in range(N):
		pan = {}
		pan['r'], pan['h'] = [decimal.Decimal(s) for s in input().split(" ")]
		pans.append(pan)
	pans.sort(key=lambda x: x['r'], reverse=True)
	# print(pans)

	ans = plate([], pans, 0, 0, K, N)

	print("Case #{}: {:.9f}".format(t, round(ans * decimal.Decimal(math.pi), 9)))
