T = int(raw_input())

def doprob():
	D, N = map(int, raw_input().split())
	horses = []
	for i in xrange(N):
		K, S = map(int, raw_input().split())
		horses.append((D - K)*1.0/S)
	time = max(horses)
	return D/time

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())