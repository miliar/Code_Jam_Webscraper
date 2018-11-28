import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

cnt_tests = int(input())



for test in range(cnt_tests):
	n, k = list(map(int, input().split()))
	units = float(input())
	v = list(map(float, input().split()))
	left = 0
	right = 1
	for i in range(200):
		mid = (left + right) / 2
		need = 0
		for x in v:
			if x < mid:
				need += (mid - x)
		if units > need:
			left = mid
		else:
			right = mid
	r = 1
	for x in v:
		if x < left:
			r *= left
		else:
			r *= x
	print('Case #%d: %.10f' % (test + 1, r))



