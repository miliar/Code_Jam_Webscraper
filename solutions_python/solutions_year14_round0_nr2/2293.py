total_cases = int(raw_input())
for case in range(0,total_cases):
	cfx = raw_input().split(' ')
	c = float(cfx[0])
	f = float(cfx[1])
	x = float(cfx[2])
	cr = 2.0
	cc = 0.0
	tt = 0.0
	tr_c = c/cr
	tr_1 = (x-cc)/cr
	tr_2 = tr_c + (x-c)/(cr+f)
	tr_p = tr_1
	while tr_2 < tr_1 and tr_1 <= tr_p:
		tt += tr_c
		cr = cr+f
		tr_c = c/cr
		tr_p = tr_1
		tr_1 = tt + (x-cc)/cr
		tr_2 = tt + tr_c + (x-c)/(cr+f)
	ret = "Case #"+str(case+1)+": " + str(tr_p)
	print ret
