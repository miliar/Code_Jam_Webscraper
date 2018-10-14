#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
	T = int(raw_input())
	for t in xrange(1,T+1):
		N, R, O, Y, G, B, V = map(int, raw_input().split())
		colors = []
		if R > 0: colors.append((R,"R"))
		if Y > 0: colors.append((Y,"Y"))
		if B > 0: colors.append((B,"B"))
		colors.sort()
		colors.reverse()

		if len(colors) == 1:
			print "Case #%d: IMPOSSIBLE"%t
		elif len(colors) >= 2:
			ok = True
			for cnt,color in colors:
				if cnt*2 > N:
					print "Case #%d: IMPOSSIBLE"%t
					ok = False
					break

			if ok:
				xs = [None]*N
				i = xs.index(None)
				for ci,(cnt,color) in enumerate(colors):
					if cnt == 0: continue
					while cnt > 0:
						xs[i] = color
						i += 2
						if i >= N:
							if None not in xs: break
							i = xs.index(None)
						cnt -= 1
					if None not in xs: break
					colors[ci] = (0,color)
				print "Case #%d:"%t, "".join(xs)
