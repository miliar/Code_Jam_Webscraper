def solve():
	N, V, T = map(float, raw_input().split())
	R0, T0 = map(float, raw_input().split())
	if N == 1:
		if T0 != T: return "IMPOSSIBLE"
		return "%.06f" % (V / R0)
	R1, T1 = map(float, raw_input().split())
	if T < min(T0, T1) or T > max(T0, T1): return "IMPOSSIBLE"
	if T0 == T1:
		return "%.6f" % (V / (R0 + R1))
	t0 = (V - V * T / T1) / (R0 - R0 * T0 / T1)
	t1 = (V * T - t0 * R0 * T0) / (R1 * T1)
	return "%.06f" % max(t0, t1)
	

for i in xrange(input()):
	print "Case #%d: %s" % (i + 1, solve())
