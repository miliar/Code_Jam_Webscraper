import math
import sys

# take the bigegst hole, go in the middle


def main():
	sys.stdin = open('input.txt', 'r')
	sys.stdout = open('output.txt', 'w')

	T = int(input())
	d = {} # memoization
	for x in range(1, T + 1):
		N, K = map(int, input().split(' '))
		(y, z) = f(N, K, d)
		print(f'Case #{x}: {y} {z}')


def f_old(N, K): # this does not work because the bathroom goers are greedy and it's not the optimal solution
	# where N is the number of stalls (minus the guards)
	# where K is the number of people
	empties = N - K # (N + 2) - (K + 2). nb empty stalls at the end
	holes = K + 1 # (K + 2) - 1
	avg_hole_size = empties / holes
	print('avg_hole_size')
	print(avg_hole_size)
	return (math.ceil(avg_hole_size), math.floor(avg_hole_size))


def f(N, K, d):
	#print(f'f({N}, {K})')
	if N < 0 or K < 0 or K > N:
		raise Exception(f'shit is wrong N={N} K={K}')
		sys.exit(1)

	if (N, K) in d:
		return d[(N, K)]

	value = None
	if K == 0:
		value = (20000000000000000000, 20000000000000000000) # i don't want to deal with nulls...
	elif K == 1:
		(left, right) = split(N - 1)
		value = (right, left)
	else:
		(N_left, N_right) = split(N - 1)
		(K_left, K_right) = split(K - 1)
		(y_left, z_left) = f(N_left, K_left, d)
		(y_right, z_right) = f(N_right, K_right, d)
		value = (min(y_left, y_right), min(z_left, z_right))
	
	d[(N, K)] = value
	return value


# Put more on the right side if you have to put more on one side.
def split(n):
	right = math.ceil(n / 2)
	left = n - right
	return (left, right)


if __name__ == '__main__':
	main()

# if k == n => easy, everything is occupied
# if k == n - 1 => 1, 0