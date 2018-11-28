from sys import stderr

def incompatible_row(c, case, i):
	for j in range(len(case[0])):
		if case[i][j] > c: return True
	return False

def incompatible_col(c, case, j):
	for i in range(len(case)):
		if case[i][j] > c: return True
	return False

def process(case):
	for i in range(len(case)):
		for j in range(len(case[0])):
			c = case[i][j]
			if incompatible_row(c, case, i) and incompatible_col(c, case, j):
				return 'NO'
	return 'YES'

def main():
	T = input()
	for i in range(T):
		N,M = tuple([int(j) for j in raw_input().split()])
		case = [[int(m) for m in raw_input().split()] for n in range(N)]
		result = process(case)
		print "Case #%d: %s" % (i+1, result)

if __name__ == '__main__': main()
