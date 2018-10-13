T = int(raw_input())

def create(path):

	count = 0

	if path == '/' or path == '':
		return 0

	if path in S:
		return 0
	else:
		f = path.rfind('/')
		count += create(path[:f])
		S.append(path)
		return count + 1

for cases in range(1,T+1):
	N, M = map(int, raw_input().split())
	count = 0
	S = ['/']
	MK = []

	for i in range(N):
		line = raw_input()
		S.append(line)

	for i in range(M):
		line = raw_input()
		count += create(line)
		#MK.append(line)

	print "Case #%d: %d" % (cases, count)
