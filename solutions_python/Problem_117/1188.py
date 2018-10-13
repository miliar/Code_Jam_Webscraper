import sys

def get_min(lawn):
	small = None
	for i in xrange(len(lawn)):
		for j in xrange(len(lawn[i])):
			if lawn[i][j] <= 100:
				if small is None or lawn[i][j] < small[0]:
					small = (lawn[i][j], i, j)
	return small

def check(lawn):
	while True:
		small = get_min(lawn)
		if small is None:
			return True
		# horizontal
		works = True
		for i in xrange(len(lawn)):
			if lawn[i][small[2]] not in (small[0], 101):
				works = False
				break
		if works:
			for i in xrange(len(lawn)):
				lawn[i][small[2]] = 101
			continue
		# vertical
		works = True
		for i in xrange(len(lawn[small[1]])):
			if lawn[small[1]][i] not in (small[0], 101):
				works = False
				break
		if works:
			for i in xrange(len(lawn[small[1]])):
				lawn[small[1]][i] = 101
			continue
		return False

lawns = int(sys.stdin.readline())
for i in xrange(1, lawns+1):
	dx, dy = [int(val) for val in sys.stdin.readline().strip().split()]
	lawn = []
	for j in xrange(dx):
		lawn.append([int(val) for val in sys.stdin.readline().strip().split()])
	outcome = "YES" if check(lawn) else "NO"
	print "Case #%d: %s" % (i, outcome)
