from __future__ import with_statement
from contextlib import nested
import sys

def gen_trees(n, A, B, C, D, X, Y, M):
	trees = set([(X,Y)])
	for i in xrange(n - 1):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		trees.add((X, Y))
	return trees

C = lambda x,y: x+y*3

def do_case(fit):
	trees = gen_trees(*map(int, fit.next().split(' ')))
	r = [0] * 9
	for tree in trees:
		r[C(tree[0]%3, tree[1]%3)] += 1
	res = 0
	for x1 in range(3):
		for y1 in range(3):
			for x2 in range(3):
				for y2 in range(3):
					x3 = (-(x1+x2))%3
					y3 = (-(y1+y2))%3
					res += r[C(x1,y1)] * r[C(x2,y2)] * r[C(x3,y3)]
	for i in range(3):
		for j in range(3):
			rs = r[C(i,j)]
			res -= rs**3
			if rs > 2:
				res += rs * (rs-1) * (rs-2)
	return res / 6

def do_all(fin, fout):
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %d\n" % (i, do_case(fit)))

if __name__ == '__main__':
	do_all(*sys.argv[1:3])
