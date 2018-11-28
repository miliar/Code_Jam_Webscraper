#!/usr/bin/env python
import sys

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for t in range(1, T+1):
		s = sys.stdin.readline().strip()
		last = '\x00'
		down = None
		for i, c in enumerate(s):
			if c < last:
				down = i
				break
			last = c
		if down is None:
			n = int(s)
		else:
			first = down - 1
			while first >= 0 and s[first] == last:
				first -= 1
			first += 1
			beg = s[:first]
			mid = s[first:down]
			end = s[down:]
			mid = chr(ord(last)-1) + '9'*(len(mid)-1)
			end = '9' * len(end)
			n = int(beg + mid + end)
		sys.stdout.write('Case #%s: %d\n' % (t, n))
