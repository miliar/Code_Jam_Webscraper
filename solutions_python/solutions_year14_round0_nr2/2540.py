def time(rate, target): return target / rate

def r(cost, ad, tg):
	t = 0
	rate = 2.0
	while time(rate, tg) > time(rate, cost) + time(rate + ad, tg):
		t += time(rate, cost)
		rate += ad
	
	t += time(rate, tg)
	return t

n = int(raw_input())
for z in range(n):
	q = map(float, raw_input().split(" "))
	print "Case #%d: %.7f" % (z + 1, r(q[0], q[1], q[2]))
