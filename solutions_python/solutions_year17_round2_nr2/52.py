def gst(a):
	res = [None]*a[0]
	bry = [(a[1], 'R'), (a[3], 'Y'), (a[5], 'B')]
	bry.sort(reverse=True)
	cur = 0
	for x, c in bry:
		for i in range(x):
			res[cur] = c
			cur += 2
			if cur >= a[0]:
				cur = 1
	return res

def cst(res):
	for i, c in enumerate(res):
		if c == res[(i+1)%len(res)]:
			return False
	return True

TC = int(input())
for tc in range(TC):
	a = list(map(int, input().split()))
	res = gst(a)
	if cst(res):
		res = ''.join(res)
	else:
		res = 'IMPOSSIBLE'
	print("Case #%d: %s" % (tc+1, res))
