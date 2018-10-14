import io
import sys


def is_pal(x):
	x = str(x)
	for i in range(len(x) // 2):
		if x[i] != x[len(x) - i - 1]:
			return False
	return True


def func(low, high):
	res = 0
	for i in range(1, 100000):
		tmp = str(i)
		
		x = tmp
		for c in reversed(tmp[:-1]):
			x += c
		x = int(x)
		sq = x * x
		if sq >= low and sq <= high and is_pal(sq):
			print(sq)
			res += 1
		if sq > high:
			break
			
	for i in range(1, 100000):
		tmp = str(i)
		
		x = tmp
		for c in reversed(tmp):
			x += c
		x = int(x)
		sq = x * x
		if sq >= low and sq <= high and is_pal(sq):
			print(sq)
			res += 1
		if sq > high:
			break
	return res


def main():
	inf = open('in.txt', 'r', encoding='utf-8')
	#inf = sys.stdin
	outf = open('out.txt', 'w', encoding='utf-8')
	#outf = sys.stdout

	first_line = inf.readline()
	print(first_line)
	T = int(first_line.rstrip())
	for test in range(T):
		N, M = inf.readline().rstrip().split()
		N = int(N)
		M = int(M)
		
		res = func(N, M)
		print('Case #' + str(test + 1) + ': ', end='', file=outf)
		print(res, file=outf)

if __name__ == '__main__':
	main()