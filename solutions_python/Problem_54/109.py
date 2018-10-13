#!/usr/bin/perl

N = int(raw_input())
for cs in range(0, N):
	aa=str.split(raw_input())
	n = int(aa[0])
	t = int(aa[1])
	d = 0;
	for i in range(1, n):
		a = int(aa[i + 1])
		tt = a - t
		if tt != 0:
			while d != 0:
				r = tt % d
				tt = d
				d = r
			d = tt
	if d < 0: d = -d
	print 'Case #' + str(cs + 1) + ': ' + str((d - t % d) % d)

