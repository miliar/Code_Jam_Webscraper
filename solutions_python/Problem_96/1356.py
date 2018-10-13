
import sys

def solve():
	result = 0
	
	l = sys.stdin.readline().split()
	l = [int(e) for e in l]
	n, s, p = l[0:3]

	for i in range(n):
		score = l[i+3]

		if score < p:
			continue

		if score >= 3 * p - 2:
			result += 1	
		elif (score == 3 * p - 3 or score == 3 * p - 4) and s > 0:
			s -= 1
			result += 1

	return result


def Main():
	test = int(sys.stdin.readline())
	for i in range(1, test+1):
		result = solve()
		print 'Case #{}: {}'.format(i, result)

if __name__ == '__main__':
	Main()