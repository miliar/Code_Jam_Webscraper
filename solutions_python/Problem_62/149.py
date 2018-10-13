import sys
import collections 

def test():
	intersects = 0
	numropes = int(sys.stdin.readline())
	ropes = [] 
	for rope in range(numropes):
		windows = map(lambda x: int(x), sys.stdin.readline().split())
		ropes.append(windows)
	ropes.sort()
	ropes = collections.deque(ropes)
	while len(ropes) > 0:
		rope = ropes.popleft()
		for otherrope in ropes:
			if (rope[0] < otherrope[0] and rope[1] > otherrope[1]) or (rope[0] > otherrope[0] and rope[1] < otherrope[1]):
				intersects += 1
	return str(intersects)

TestCases = int(sys.stdin.readline())
for testCase in range(TestCases):
	print "Case #"+str(testCase+1)+": "+test()
