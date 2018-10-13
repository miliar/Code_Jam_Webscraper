#!/usr/bin/env python
# coding: utf-8

from __future__ import division

"""
* You start with 0 cookies, but producing 2 cookies per second.
* After 250 seconds, you will have C=500 cookies and can buy a farm that produces F=4 cookies per second.
* After buying the farm, you have 0 cookies, and your total cookie production is 6 cookies per second.
* The next farm will cost 500 cookies, which you can buy after about 83.3333333 seconds.
* After buying your second farm, you have 0 cookies, and your total cookie production is 10 cookies per second.
* Another farm will cost 500 cookies, which you can buy after 50 seconds.
* After buying your third farm, you have 0 cookies, and your total cookie production is 14 cookies per second.
* Another farm would cost 500 cookies, but it actually makes sense not to buy it: instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.

Limits
------

1 ≤ T ≤ 100.
Small dataset

1 ≤ C ≤ 500.
1 ≤ F ≤ 4.
1 ≤ X ≤ 2000.
Large dataset

1 ≤ C ≤ 10000.
1 ≤ F ≤ 100.
1 ≤ X ≤ 100000.
"""

if __name__ == '__main__':
    with open('B-small-attempt0.in') as handle:
        _ = handle.next()
        for j, line in enumerate(handle, start=1):
            C, F, X = map(float, line.strip().split(' '))
            def velocity(i):
                return 2 + i * F
            farms = 0
            previous = X / velocity(farms)
            while True:
                current = sum([(C / velocity(i)) for i in range(farms)]) + (X / velocity(farms))
                if previous < current:
                    print('Case #%s: %0.7f' % (j, previous))
                    break
                previous = current
                farms += 1

