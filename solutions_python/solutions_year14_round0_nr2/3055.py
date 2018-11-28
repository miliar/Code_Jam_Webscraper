from __future__ import division

def solve(C, F, X):
    t_sofar = 0
    f = 0
    p = 2
    while (True):
        t_nobuy = X/p
        t_tobuy = C/p
        t_withbuy = t_tobuy + X/(p+F)
        if (t_nobuy < t_withbuy):
            return t_sofar + t_nobuy
        t_sofar += t_tobuy
        f += 1
        p += F

def main(lines):
    T = lines.pop(0)
    case = 1
    for l in lines:
        print "Case #%d: %f" % (case, solve(*(float(x) for x in l.split())))
        case += 1

if __name__ == '__main__':
    main(open('input.txt').readlines())