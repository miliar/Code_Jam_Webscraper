import sys, math

sys.stdin = open('A-small-attempt1.in')

def solve(sarr):
	result, peoples = 0, 0

	for index, item in enumerate(sarr):
		if item and index > peoples:
			result += index - peoples
			peoples += result
		peoples += item
	return result

T = int(sys.stdin.readline())

for i in xrange(T):
	mx, data = sys.stdin.readline().split()
	data = map(int,data)
	print 'Case #' + str(i+1) + ': ' + str(solve(data))