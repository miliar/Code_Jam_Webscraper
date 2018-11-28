import sys
import bisect

get_line = lambda: sys.stdin.readline()


def solve_case():
    C, F, X = map(lambda x: float(x), get_line().split())
    time = 0.
    rate = 2.
    while C/rate + X/(rate + F) < X/rate:
        time += C/rate
        rate += F
    time += X/rate
    return " %.7f" % time

def main():
    T = int(get_line())
    for i in xrange(T):
        print "Case #%d:" % (i + 1) + solve_case()

if __name__ == '__main__':
    main()




