#!/usr/bin/python

import sys

f = open(sys.argv[1])
T = int(f.readline().strip())
for t in range(1, T+1):
    N = f.readline().strip()
    C = []
    for c in N: C.append(c)
    i = len(C) - 1
    max = C[i]
    imax = i
    while True:
	i -= 1
	if i < 0: break
	if C[i] < max: break
	if C[i] > max:
	    max = C[i]
	    imax = i
    if i < 0:
	C.sort()
	j = 0
	while j < len(C) and C[j] == '0': j+=1
	O = [C[j]] + ['0'] + C[0:j] + C[j+1:]
    else:
	m = max
	jm = imax
	for j in range(i + 1, len(C)):
	    if C[j] != '0' and C[j] < m and C[j] > C[i]:
		m = C[j]
		jm = j
	O = C[0:i] + [m] + sorted(C[i+1:jm] + [C[i]] + C[jm+1:])
    o = ''.join(O)
    print 'Case #%d: %s' % (t, o)
