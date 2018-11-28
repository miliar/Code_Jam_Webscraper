tc = int(raw_input())
for ct in range(1,tc+1):
	ans = 0

	d = raw_input().split()
	a = int(d[0])
	b = int(d[1])
	if b > 11:
		for j in range(1,10):
			cj = str(j)
			for k in range(0,10):
				ck = str(k)
				n =    int(cj+ck)
				if n >= a:
					inv = int(ck+cj)
					if inv > n and inv <= b:
						ans += 1
		if b > 100:
			for i in range(0,10):
				ci = str(i)
				for j in range(0,10):
					cj = str(j)
					for k in range(0,10):
						ck = str(k)
						n =    int(ci+cj+ck)
						if n >= a:
							inv1 = int(ck+ci+cj)
							inv2 = int(cj+ck+ci)
							if inv1 > n and inv1 <= b:
								ans += 1
							if inv2 > n and inv2 <= b:
								ans += 1
	
	print "Case #" + str(ct) + ": " + str(ans)
