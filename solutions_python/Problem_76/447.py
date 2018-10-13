def int_input():
	return int(raw_input())

def list_int_input():
	return [int(ch) for ch in raw_input().split()]

def can_split(candies):
	xor = 0
	for candy in candies:
		xor = xor ^ candy
	return xor == 0

def solve(c):
	int_input()
	candies = list_int_input()
	if can_split(candies):
		print 'Case #%d: %d' % (c, sum(candies)-min(candies))
	else:
		print 'Case #%d: NO' % c

def main():
	for c in range(int_input()):
		solve(c+1)

main()

