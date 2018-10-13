def case(file):
	c = set(range(1, 17))
	for t in range(2):
		v = int(file.readline())
		m = [[int(x) for x in file.readline().strip().split()] for i in range(4)]
		c.intersection_update(m[v - 1])
	if len(c) == 1:
		return str(list(c)[0])
	elif len(c) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"



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

cases("A-small-attempt0.in", stdout=0)