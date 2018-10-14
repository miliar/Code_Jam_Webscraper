# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2017-04-09 05:32:12
# @Last Modified by:   shubham
# @Last Modified time: 2017-04-09 06:03:39

from collections import defaultdict

def partition(n):
	if n%2 == 0:
		return n//2, n//2 - 1
	else:
		return (n-1)//2, (n-1)//2


def main():
	for t in range(int(input())):
		n, k = list(map(int, input().split()))

		lr = defaultdict(int)
		lr[n] = 1

		for i in range(k):
			which = max(lr.keys())
			lr[which] -= 1

			if lr[which] == 0:
				del lr[which]

			x, y = partition(which)
			lr[x] += 1
			lr[y] += 1
		
		print('Case #{}: {} {}'.format(t+1, x, y))

if __name__ == '__main__':
	main()

