from __future__ import division
import sys
sys.setrecursionlimit(10000)
# cookie clicker
EXAMPLE_IN = """\
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
"""

EXAMPLE_OUT = """\
Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
"""


def solve(farm_cost, farm_gain, cookie_goal, rate=2.0):
    farm_time_so_far = 0.0
    while True:
        max_time = cookie_goal/rate
        farm_time = farm_cost/rate
        max_time_with_farm = farm_time + cookie_goal/(rate+farm_gain)
    # print >> sys.stderr, 'DEBUG mt: %9.6f mtf: %9.6f rate: %3.0f' % (max_time, max_time_with_farm , rate)
        if max_time <= max_time_with_farm:
            return farm_time_so_far + max_time
        farm_time_so_far += farm_time
        rate += farm_gain

def main(lines):
    for i in xrange(int(next(lines))):
        args = map(float, next(lines).split())
        ans = 'Case #%d: %s' % (i+1, solve(*args))
        print ans

#    test_cases = [lines[i*4for i in range(cases)]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
    else:
        input = open(sys.argv[1])
    main(input)
