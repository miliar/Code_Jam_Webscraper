def Solve():
	def AddToSet(s, d):
		cur = ''
		for t in d.split('/')[1:]:
			cur += '/' + t
			s.add(cur)
	have, want = map(int, raw_input().split())
	haveSet = set()
	wantSet = set()
	for _ in range(have):
		AddToSet(haveSet, raw_input())
	for _ in range(want):
		AddToSet(wantSet, raw_input())
	#print haveSet
	#print wantSet
	return len(wantSet.difference(haveSet))

for tc in range(1, int(input()) + 1):
	print("Case #%d: %s" % (tc, Solve()))