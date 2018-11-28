
def solve():
	x,r,c = map(int, raw_input().split())
	if c<r:
		r,c = c,r
	A     = r*c
	if A%x != 0:
		return 1
	if x<=2:
		return 0
	if x==3:
		if r<2 or c<2:
			return 1
		return 0
	if x==4:
		if r==4 and c==4:
			return 0
		if r==3 and c==4:
			return 0
		if r==4 and c==3:
			return 0
		return 1

def main():
	T = int(raw_input())
	msg = ["GABRIEL", "RICHARD"]
	for tc in xrange(1,T+1):
		ret = solve()
		print "Case #%d: %s" % (tc,msg[ret])

main()
