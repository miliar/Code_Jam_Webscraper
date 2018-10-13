#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(n, s):
    n = int(n)
    n += 1
    l = list(s)
    l[0] = int(l[0])
    total = l[0]
    ret = 0
    for i in range(1, n):
	l[i] = int(l[i])
	if total < i and i - total > ret:
	    ret = i - total
	total += l[i]
    return ret

def main():
    T = int(raw_input(''))
    for i in range(T):
	n, s = raw_input('').split(' ')
	res = solve(n, s)
	print 'Case #%d: %d' % (i + 1, res)

if __name__ == '__main__':
    main()
