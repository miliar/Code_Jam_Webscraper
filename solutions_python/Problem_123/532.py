from sys import *

def needs_motes(A, mote):
	needs = 0
	while A <= mote:
		A += A - 1
		needs += 1
	return (needs, A)

def test():
	line = stdin.readline().split(' ')
	A = int(line[0])
	N = int(line[1])
	motes = []
	line = stdin.readline().split(' ')
	for n in range(N):
		motes.append(int(line[n]))
	motes.sort()

	if A == 1:
		return len(motes)

	cur = 0
	mod = 0
	while cur < len(motes):
		if A <= motes[cur]:
			needs, A = needs_motes(A, motes[cur])
			if needs > len(motes) - cur:
				return mod + len(motes) - cur
			else:
				mod += needs
		A += motes[cur]
		cur += 1

	return mod

T = int(stdin.readline())
for t in range(T):
	res = test()
	print 'Case #%d: %d' % (t + 1, res)
