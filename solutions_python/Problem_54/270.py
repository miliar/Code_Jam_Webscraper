#!/usr/bin/env python

import sys

gcd = lambda x, y: y and gcd(y, x % y) or x

def fair_warning(t):
	m = map(lambda x: x - t[0], t)
	x = 0
	for n in m[1:]:
		x = gcd(x, n)
	a = t[0] // x
	if a * x == t[0]: return 0
	return (a + 1) * x - t[0]

def main(args):
	f = file(args[1])
	fout = file(args[2], "w")
	C = int(f.readline().strip())
	for i, l in enumerate(f):
		t = sorted(map(int, l.strip().split()[1:]))
		print >>fout, "Case #%d: %d" % (i + 1, fair_warning(t))

#if __name__ == "__main__": main(sys.argv)
#if __name__ == "__main__": main(["", "test.in"])
#if __name__ == "__main__": main(["", "B-small-attempt0.in", "B-small-attempt0.out"])
if __name__ == "__main__": main(["", "B-large.in", "B-large.out"])
