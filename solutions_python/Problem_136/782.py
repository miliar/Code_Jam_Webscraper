
def solve():
	ntest = int(raw_input())
	for t in range(0,ntest):
		ip = raw_input().split(" ")
		price = float(ip[0])
		drate = float(ip[1])
		target = float(ip[2])
		nfarm = 0
		t0 = 0.0
		rate = 2.0
		t_old = target
		while True:
			t_curr = target / rate + t0
			#print nfarm, rate, t_curr
			if t_curr >= t_old:
				t_curr = t_old
				break
			else:
				t_old = t_curr
				nfarm = nfarm + 1
				t0 = t0 + (price / rate)
				rate = rate + drate
		print "Case #%d: %.10f" % (t+1, t_curr)

if __name__ == "__main__":
	solve()
