import sys

def main():
	sys.stdin = open('input.txt', 'r')
	sys.stdout = open('output.txt', 'w')
	# numbers = list(map(int, input().split(' ')))

	T = int(input())
	for x in range(1, T + 1):
		[D, N] = list(map(int, input().split(' ')))
		data = []
		for _ in range(N):
			[K, S] = list(map(int, input().split(' ')))
			data.append((K, S))
		y = f(data, D)
		print(f'Case #{x}: {y}')


def f(data, destination):
	max_t = 0
	for (pos, speed) in data: # (K, S)
		t = (destination - pos) / speed # arrival time for horse
		max_t = max(max_t, t)
	return destination / max_t


if __name__ == '__main__':
	main()