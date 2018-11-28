#!/usr/bin/python

import sys, re
rl = sys.stdin.readline

if __name__ == '__main__':
	tests = int(rl())

	for case in xrange(1, tests + 1):
		data, chunks = rl().split(), []

		for x in range(2):
			nr = int(data.pop(0))
			chunks.append([data.pop(0) for x in range(1, nr + 1)])

		(c, d), n, result = chunks, data[-1], ''

		if c:
			c = dict([('%c%c' % (a, b), c) for a, b, c in [list(x) for x in c]])

		if d:
			d = [re.compile('%c[^%c]*%c' % (start, stop, stop)) for start, stop in d]

		for invoke in list(n):
			result += invoke
			chunk = result[-2:]

			if c:
				combine = filter(None, [c.get(code) for code in [chunk, chunk[::-1]]])

				if combine:
					result = result[:-2] + combine[0]

			if d:
				for regexp in d:
					if re.search(regexp, result) or re.search(regexp, result[::-1]):
						result = ''
						break

		print 'Case #%d: [%s]' % (case, ', '.join(result))
