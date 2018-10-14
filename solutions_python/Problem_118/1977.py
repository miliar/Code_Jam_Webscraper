a = [1,
 4,
 9,
 121,
 484,
 10201,
 12321,
 14641,
 40804,
 44944,
 1002001,
 1234321,
 4008004,
 10000200001L,
 10221412201L,
 12102420121L,
 12345654321L,
 40000800004L,
 100000020000001L]

with open('input.txt', 'rt') as f:
	tests = map(lambda x: map(int,x.split(' ')), f.readlines()[1:])

with open('output.txt', 'wt') as o:
	for i, t in enumerate(tests):
		ans = len(filter(lambda x: t[0] <= x <=t[1], a))
		o.write("Case #%i: %i\n" % (i+1, ans))
