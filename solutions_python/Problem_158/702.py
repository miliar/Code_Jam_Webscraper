def ominoes(X, R, C):
	if X == 1:
		return 'GABRIEL'

	if X == 2:
		if R * C % 2 == 0:
			return 'GABRIEL'
		return 'RICHARD'

	if X == 3:
		if R * C % 3 == 0 and R * C > 3:
			return 'GABRIEL'
		return 'RICHARD'

	if X == 4:
		if R * C % 4 == 0 and R * C > 8:
			return 'GABRIEL'
		return 'RICHARD'

def main():
	from sys import stdin
	input = stdin.read().split('\n')
	T = int(input[0])

	for t in range(T):
		X, R, C = map(int, input[t+1].split())

		print "Case #{0}: {1}".format(t + 1, ominoes(X, R, C))

if __name__ == '__main__':
	main()