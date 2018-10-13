# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2017-04-22 21:52:52
# @Last Modified by:   shubham
# @Last Modified time: 2017-04-22 21:58:03


for t in range(int(input())):
	D, N = list(map(int, input().split()))

	max_val = float('-inf')
	for _ in range(N):
		a,b = list(map(int, input().split()))
		max_val = max(max_val, (D-a)/b)

	print("Case #{}: {}".format(t+1, D/max_val))
