# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2017-04-09 03:00:40
# @Last Modified by:   shubham
# @Last Modified time: 2017-04-09 03:36:06


def non_decreasing(n):
	n = str(n)
	return all(x<=y for x, y in zip(n, n[1:]))

def tidy(n):
	n = list(map(int, str(n)))
	for idx in range(len(n)-1):
		if n[idx] > n[idx+1]:
			break
	
	n[idx] -= 1
	for i in range(idx+1, len(n)):
		n[i] = 9

	return int(''.join(map(str, n)))


def main():
	for t in range(int(input())):
		n = int(input())
		while not non_decreasing(n):
			n = tidy(n)
		print('Case #{}: {}'.format(t+1, n))


if __name__ == '__main__':
	main()
	# tidy(7753)

