#!/usr/bin/env python

import math, sys

def solve():
	flyRadius, racketRadius, racketBorder, stringRadius, gap = (
		float(s) for s in sys.stdin.readline().split()
		)

	# Simplify by pretending the fly is a point.
	racketBorder += flyRadius
	stringRadius += flyRadius
	gap -= 2 * flyRadius

	# Because the racket is symmetric in two directions, we only have to
	# look at one quarter.

	missArea = 0.0
	racketInner = racketRadius - racketBorder
	racketInnerSq = racketInner ** 2
	gridSpacing = 2 * stringRadius + gap
	numStrings = int(racketInner / gridSpacing) + 1 # round up
	for gridX in range(numStrings):
		x0 = gridSpacing * gridX + stringRadius
		x1 = x0 + gap
		for gridY in range(numStrings):
			y0 = gridSpacing * gridY + stringRadius
			y1 = y0 + gap
			d0 = x0 ** 2 + y0 ** 2
			d1 = x1 ** 2 + y1 ** 2
			if d0 > racketInnerSq:
				# Grid cell is entirely outside.
				pass
			elif d1 < racketInnerSq:
				# Grid cell is entirely inside.
				missArea += gap ** 2
			else:
				# Grid cell is partially inside.
				cx0 = math.sqrt(racketInnerSq - y0 ** 2)
				cx1 = math.sqrt(max(racketInnerSq - y1 ** 2, 0.0))
				cy0 = math.sqrt(racketInnerSq - x0 ** 2)
				cy1 = math.sqrt(max(racketInnerSq - x1 ** 2, 0.0))
				if cx1 > x0:
					# Full grid height section.
					missArea += (cx1 - x0) * gap
				# Partial section.
				# h(x) = sqrt(racketInnerSq - x ** 2) - y0
				px0 = max(x0, cx1)
				px1 = min(x1, cx0)
				a = math.asin(px0 / racketInner) * 2
				b = math.asin(px1 / racketInner) * 2
				missArea += (racketInnerSq / 4) * (
					(math.sin(b) + b) - (math.sin(a) + a)
					) - y0 * (px1 - px0)
				# Remaining section (if any) contributes 0.

	totalArea = math.pi * racketRadius ** 2 / 4
	return '%1.6f' % (1.0 - (missArea / totalArea))

cases = int(sys.stdin.readline())
for case in range(cases):
	print 'Case #%d: %s' % (case + 1, solve())
