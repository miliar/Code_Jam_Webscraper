# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2017-04-09 04:14:55
# @Last Modified by:   shubham
# @Last Modified time: 2017-04-09 05:20:50

def flip(arr):
	return [1-ele for ele in arr]

def main():
	for t in range(int(input())):
		pancakes, k = input().split()
		k = int(k)
		z = list(map(int, pancakes.replace('+', '1').replace('-', '0')))
		# print(z)

		cnt = 0
		for i in range(len(z)-k+1):
			if z[i] == 0:
				z[i:i+k] = flip(z[i:i+k])
				cnt += 1

		if set(z) == {1}:
			print('Case #{}: {}'.format(t+1, cnt))
		else:
			print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE'))
				

if __name__ == '__main__':
	main()

