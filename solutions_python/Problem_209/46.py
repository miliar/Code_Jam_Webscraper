import math

t = int(input())

for case in range(1,t+1):
	n, k = [int(x) for x in input().split()]
	arr = []
	for i in range(n):
		arr.append([int(x) for x in input().split()])
	arr = sorted(arr, key=lambda x:x[0]*x[1], reverse=True)
	arr_f, arr_s = arr[:k], arr[k:]

	ans1 = sum(x[0]*x[1] for x in arr[:k])*2 + max(x[0] for x in arr[:k])**2
	if len(arr[k-1]) > 0:
		max_r = max(x[0] for x in arr[:k-1]) if k>1 else 0
		fir_pan = [x for x in arr[k-1:] if x[0] > max_r]
		ans2 = sum(x[0]*x[1] for x in arr[:k-1])*2 + max(x[0]**2+x[0]*x[1]*2 for x in arr[k-1:]) if len(fir_pan) else 0
	else:
		ans2 = 0
	# print(ans1, ans2)

	print('Case #%d: %.10f' % (case, max(ans1,ans2)*math.pi))
