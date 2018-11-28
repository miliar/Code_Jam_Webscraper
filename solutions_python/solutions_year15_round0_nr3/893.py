import sys

MAPPING = {
	'1': {
		'1': ('1', 1),
		'i': ('i', 1),
		'j': ('j', 1),
		'k': ('k', 1),
	},
	'i': {
		'1': ('i', 1),
		'i': ('1', -1),
		'j': ('k', 1),
		'k': ('j', -1),
	},
	'j': {
		'1': ('j', 1),
		'i': ('k', -1),
		'j': ('1', -1),
		'k': ('i', 1),
	},
	'k': {
		'1': ('k', 1),
		'i': ('j', 1),
		'j': ('i', -1),
		'k': ('1', -1),
	},
}

def multQ(a, b):
	mapping = MAPPING[a[0]][b[0]]
	return (mapping[0], mapping[1] * a[1] * b[1])

def simplify(vals, X):
	step = 0;

	val = ('1', 1)
	for i in xrange(X):
		for c in vals:
			val = multQ(val, c)

			if step == 0 and val[0] == 'i' and val[1] == 1:
				step = 1
			elif step == 1 and val[0] == 'k' and val[1] == 1:
				step = 2
			elif step == 2 and val[0] == '1' and val[1] == -1:
				step = 3

	if step != 3: return False

	return val[0] == '1' and val[1] == -1


# Since the file structure is 100% ensured, just skip the line count
T = int(sys.stdin.readline().strip())

for i in xrange(T):
	[L, X] = sys.stdin.readline().strip().split(' ')
	vals = [(c, 1) for c in sys.stdin.readline().strip()]

	valid = simplify(vals, int(X))

	# i*j*k == -1, so we just need to ensure that the final result is -1.
	print "Case #%d: %s" % (i + 1, valid and 'YES' or 'NO')
