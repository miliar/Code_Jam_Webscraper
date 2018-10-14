#!/usr/bin/env python

import sys
from math import pi, sqrt, acos

def sqr(num):
    return num * num

def calcIntersection(a, b, R, x, y, h):
    result = (b * sqrt(sqr(R) - sqr(b)) -
              a * sqrt(sqr(R) - sqr(a)) +
              sqr(R) * (acos(a / R) - acos(b / R))
              ) / 2.0 - y * (b - a) + h * (a - x)

    return result

def calcProbability(flyRadius, outerRadius, thickness, stringRadius, gapSize):
    flyDiameter = flyRadius * 2.0

    if gapSize < flyDiameter:
        return 1.0

    effectiveRadius = outerRadius - thickness - flyRadius;
    effectiveGapSize = gapSize - flyDiameter
    effectiveStringRadius = stringRadius + flyRadius

    outerArea = pi * sqr(outerRadius)

    gapsArea = 0.0

    dist_R = sqr(effectiveRadius)

    y_low = effectiveStringRadius

    while y_low < effectiveRadius:
        y_hi = y_low + gapSize - flyDiameter

        x_low = effectiveStringRadius
        while x_low < effectiveRadius:
            x_hi = x_low + gapSize - flyDiameter

            dist_ll = sqr(x_low) + sqr(y_low)
            if dist_ll > dist_R:
                break

            dist_lh = sqr(x_low) + sqr(y_hi)
            dist_hl = sqr(x_hi) + sqr(y_low)
            dist_hh = sqr(x_hi) + sqr(y_hi)

            if dist_hh <= dist_R:
                gapsArea += sqr(effectiveGapSize)
            else:
                a = x_low
                b = x_hi

                if dist_lh < dist_R:
                    a = sqrt(dist_R - sqr(y_hi))

                if dist_hl > dist_R:
                    b = sqrt(dist_R - sqr(y_low))

                gapsArea += calcIntersection(a, b, effectiveRadius, x_low, y_low, effectiveGapSize)

            x_low += 2.0 * stringRadius + gapSize

        y_low += 2.0 * stringRadius + gapSize

    gapsArea *= 4.0

    return 1.0 - gapsArea / outerArea

def main():
    if len(sys.argv) == 1:
        f = open('test.in')
    else:
        f = open(sys.argv[1])

    count = int(f.readline())
    for i in xrange(1, count + 1):

        items = f.readline().strip().split(' ')

        flyRadius = float(items[0])
        outerRadius = float(items[1])
        thickness = float(items[2])
        stringRadius = float(items[3])
        gapSize = float(items[4])

        probability = calcProbability(flyRadius, outerRadius, thickness, stringRadius, gapSize)
        print 'Case #%d: %.6f' % (i, probability)

if __name__ == '__main__':
    main()
