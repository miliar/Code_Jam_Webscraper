from __future__ import with_statement
from contextlib import nested
import sys


def to_minutes(tm):
	h,m = map(int, tm.split(':'))
	return h*60 + m

def load_table(fit, n, a_sch, b_sch, tat):
	for i in range(n):
		dep, arr = map(to_minutes, fit.next().split(' '))
		a_sch.append((dep, 1))
		b_sch.append((arr + tat, -1))

def count_trains(sch):
	sch.sort()
	avail, req = 0, 0
	for t in sch:
		avail += t[1]
		req = max(avail, req)
	return req

def do_case(fit):
	tat = int(fit.next())
	a_sch, b_sch = [], []
	a_n, b_n = map(int, fit.next().split(' '))
	load_table(fit, a_n, a_sch, b_sch, tat)
	load_table(fit, b_n, b_sch, a_sch, tat)
	return count_trains(a_sch), count_trains(b_sch)

def do_all(fin, fout):
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %d %d\n" % ((i,) + do_case(fit)))

if __name__ == '__main__':
	do_all(*sys.argv[1:3])
