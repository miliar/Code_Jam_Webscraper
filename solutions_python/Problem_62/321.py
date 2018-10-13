def inter(w1, w2):
	return (w1[0] > w2[0] and w1[1] < w2[1]) or (w1[0] < w2[0] and w1[1] > w2[1])

def intersect(ws):
	ans = 0
	while True:
		w = ws.pop()
		if len(ws) == 0:
			break
		else:
			for i in ws:
				if inter(w, i): ans += 1
	return ans

T = int(raw_input())
for t in xrange(1, T + 1):
	N = int(raw_input())
	wire = []
	for n in xrange(N):
		wire.append([int(i) for i in raw_input().split()])
	print "Case #%d: %d" % (t, intersect(wire))
