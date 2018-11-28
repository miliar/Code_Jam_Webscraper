def case(file):
	import math
	r0 = 2
	[c, f, x] = [float(x) for x in file.readline().strip().split()]
	k = max(math.floor((x-c)/c-r0/f) + 1, 0)
	t = sum(c/(r0+i*f) for i in range(k)) + x/(r0+k*f)
	return '%.7f' % t



def cases(in_name, func=None, out_name=None, stdout=None):
	import sys
	if func is None:
		func = case
	if out_name is None:
		ext = in_name.rindex('.')
		out_name = in_name[:ext] + ".out"
	with open(in_name, 'r') as fin:
		with stdout and sys.stdout or open(out_name, 'w') as fout:
			ntests = int(fin.readline())
			for i in range(1, ntests + 1):
				fout.write("Case #%i: %s\n" % (i, func(fin)))

cases("B-large.in", stdout=0)