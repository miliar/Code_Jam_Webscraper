import decimal
T = int(raw_input().strip())
T_counter = 1
while T_counter <= T:
	line = raw_input().strip().split(' ')
	L = decimal.Decimal(line[0])
	P = decimal.Decimal(line[1])
	C = decimal.Decimal(line[2])
	ans = 0
	while L * C < P:
		L = L * (P / L).sqrt()
		ans = ans + 1
	print "Case #%d: %d" % (T_counter, ans)
	T_counter = T_counter + 1
