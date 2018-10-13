
def GetFuncMin(C, F, X):
	n = 0
	t_c0 = C/2
	t_t0 = t_c0 + X/(2+(n+1)*F)
	while (1):
		n += 1
		t_c1 = t_c0+C/(2+n*F)
		t_t1 = t_c1 + X/(2+(n+1)*F)
		if (t_t1 > t_t0):
			break
		t_c0 = t_c1
		t_t0 = t_t1
	return t_t0

for case in xrange(input()):
	C, F, X = map(float, raw_input().split(' '))
	t_base = X/2.0
	t_compra = GetFuncMin(C, F, X)

	print 'Case #%d: %f' % ((case+1), min([t_base, t_compra]))

