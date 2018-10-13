def toInt(s):
	return int(float(s) * 10000 + 0.5)

def main(testNo):
	n, v, x = raw_input().split()
	n, v, x = int(n), toInt(v), toInt(x)
	r = []
	c = []
	for i in xrange(n):
		a, b = map(toInt, raw_input().split())
		r.append(a)
		c.append(b)
	if n == 1:
		if x == c[0]:
			print "Case #%d: %.20f" % (testNo, float(v) / r[0])
		else:
			print "Case #%d: IMPOSSIBLE" % testNo
	elif n == 2:
		# quick kill:
		if not min(c[0], c[1]) <= x <= max(c[0], c[1]):
			print "Case #%d: IMPOSSIBLE" % testNo
			return
		elif c[0] == c[1] == x:
			print "Case #%d: %.20f" % (testNo, float(v) / (r[0] + r[1]))
			return
		elif c[0] == x:
			print "Case #%d: %.20f" % (testNo, float(v) / r[0])
			return
		elif c[1] == x:
			print "Case #%d: %.20f" % (testNo, float(v) / r[1])
			return
		A, B, C, D, E, F = r[0], r[1], v, r[0] * c[0], r[1] * c[1], v * x
		d = A * E - B * D
		if d == 0:
			dx = C * E - B * F
			dy = A * F - C * D
			if dx != 0 or dy != 0:
				print "Case #%d: IMPOSSIBLE" % testNo
				return
			t = float(C) / max(A, B)
			print "Case #%d: %.20f" % (testNo, t)
			return
		dx = C * E - B * F
		dy = A * F - C * D
		if dx * d < 0 or dy * d < 0:
			print "Case #%d: IMPOSSIBLE" % testNo
			return
		t0 = float(dx) / d
		t1 = float(dy) / d
		print "Case #%d: %.20f" % (testNo, max(t0, t1))

	else:
		pass

T = int(raw_input())
for testNo in xrange(1, T + 1):
	main(testNo)