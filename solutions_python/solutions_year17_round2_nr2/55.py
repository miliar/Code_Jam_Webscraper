num_case = int(input())

def solve():
	n, r, o, y, g, b, v = map(int, input().split())

	if o == 0 and g == 0 and  v == 0:
		arr = sorted([[r, 'R'], [y, 'Y'], [b, 'B']])
		if arr[2][0] > arr[0][0]+arr[1][0]:
			return "IMPOSSIBLE"

		ret = ''

		diff = arr[1][0]-arr[0][0]
		ret += (arr[2][1]+arr[1][1])*diff
		arr[2][0] -= diff
		arr[1][0] -= diff

		half = arr[2][0] // 2
		ret += (arr[2][1]+arr[0][1])*half + (arr[2][1]+arr[1][1])*(arr[2][0]-half)
		arr[1][0] -= arr[2][0]-half
		arr[0][0] -= half
		arr[2][0] = 0

		ret += (arr[0][1]+arr[1][1])*arr[1][0]
		arr[0][0] -= arr[1][0]
		arr[1][0] = 0

		if arr[0][0]:
			ret += arr[0][1]
			arr[0][0] = 0

		return ret
	else:
		return "SOLVE SMALL"

for now_case in range(1, num_case+1):
	print("Case #{}: {}".format(now_case, solve()))