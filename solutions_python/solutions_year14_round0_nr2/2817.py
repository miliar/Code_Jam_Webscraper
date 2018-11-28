import sys
import re


inf = sys.stdin
outf = sys.stdout

R = 2.0
MAX_X = 100000


def handle_case(case_num):
    C, F, X = map(float, inf.readline().strip().split())

    rate = R
    next_rate = rate + F
    cur_t = 0.

    while True:
        t = X / rate
        next_t = C / rate + X / next_rate
        if next_t >= t:
            res = t + cur_t
            break
        else:
            cur_t += C / rate
            rate = rate + F
            next_rate = next_rate + F
    case_str = 'Case #{0}: {1}'.format(case_num, res)
    print >>outf, case_str


def main():
    if len(sys.argv) > 1:
        global inf
        inf = open(sys.argv[1])
    if len(sys.argv) > 2:
        global outf
        outf = open(sys.argv[2], 'w')

    T = int(inf.readline().strip())
    for case_num in xrange(1, T + 1):
        handle_case(case_num)

    if inf != sys.stdin:
        inf.close()
    if outf != sys.stdout:
        outf.close()


if __name__ == '__main__':
    main()
