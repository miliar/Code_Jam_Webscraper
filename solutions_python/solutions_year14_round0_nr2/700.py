T = int(raw_input())

for t in range(T):
	tmp = (raw_input()).split(" ")
	
	C = float(tmp[0])
	F = float(tmp[1])
	X = float(tmp[2])
	cps = 2.0
	
	ans = 0.0
	while X / cps > C / cps + X / (cps + F):
		ans += C / cps
		cps += F
	
	print 'Case #' + str(t+1) + ': ' + '{:.7f}'.format(ans + X / cps)
