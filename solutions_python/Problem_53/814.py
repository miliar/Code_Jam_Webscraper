# -*- coding: utf-8 -*-
# !/usr/bin/python

fIn = open('Input', 'r')
n = int(fIn.readline())
nbr = [[int(a) for a in fIn.readline().split()] for i in xrange(n)]
fIn.close()

fOut = open('Output', 'w')
i = 0
while i < len(nbr):
	a = 2**nbr[i][0] - 1
	out = 'Case #' + str(i + 1) + ': '
	if nbr[i][1] % (a + 1) == a % (a + 1):
		out += 'ON'
	else:
		out += 'OFF'

	fOut.write(out + '\n')

	i += 1
fOut.close()
