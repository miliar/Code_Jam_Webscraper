
def solve(a,b,grids):
	numberset = set(grids[0][a])
	numberset &= set(grids[1][b])
	return numberset

T = int(raw_input())
for t in xrange(1,T+1):
	a = int(raw_input())-1
	grids = []
	grids.append(
		[map(int,raw_input().split()) for _ in xrange(4)]
	)
	b = int(raw_input())-1
	grids.append(
		[map(int,raw_input().split()) for _ in xrange(4)]
	)

	numberset = solve(a,b,grids)
	if len(numberset)>1:
		print "Case #%d: Bad magician!" % (t)
	elif len(numberset)==1:
		print "Case #%d: %d" % (t, list(numberset)[0])
	else:
		print "Case #%d: Volunteer cheated!" % (t)
