import sys


def get_trees(n, A, B, C, D, x0, y0, M):
	trees = []
	X = x0
	Y = y0
	trees.append((X, Y))
	for i in xrange(n - 1):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		trees.append((X, Y))
	return trees


def get_triangles(trees):
	count = 0
	for ind1 in xrange(len(trees)):
		for ind2 in xrange(ind1 + 1, len(trees)):
			for ind3 in xrange(ind2 + 1, len(trees)):
				v1 = trees[ind1]
				v2 = trees[ind2]
				v3 = trees[ind3]
				if (((v1[0] + v2[0] + v3[0]) % 3) == 0) and (((v1[1] + v2[1] + v3[1]) % 3) == 0):
#					print v1, v2, v3
					count += 1
	return count


def fread():
    try:
        inp = open(sys.argv[1], 'rt')
    except IOError:
        print 'Invalid input filename'
        sys.exit(2)

    out = open(sys.argv[2], 'wt')

    ncases = int(inp.readline())

    for i in xrange(ncases):
        print i
        args = map(int, inp.readline().split())
        out.write('Case #%d: %d\n' % (i + 1, get_triangles(get_trees(*args))))

    inp.close()
    out.close()


if __name__ == '__main__':
#	print get_triangles(get_trees(6, 2, 0, 2, 1, 1, 2, 11))
	fread()

