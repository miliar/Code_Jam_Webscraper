from __future__ import with_statement
from contextlib import nested
import sys

def count_switches(queries, eng_num):
	n = 0
	s = set()
	for q in queries:
		s.add(q)
		if len(s) == eng_num:
			n += 1
			s = set((q,))
	return n

def do_case(fit):
	eng_num = int(fit.next())
	for i in range(eng_num): fit.next()
	qs_num = int(fit.next())
	return count_switches((fit.next().strip('\n\r') for i in range(qs_num)), eng_num)

def do_all(fin, fout):
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %d\n" % (i, do_case(fit)))

if __name__ == '__main__':
	do_all(*sys.argv[1:3])
