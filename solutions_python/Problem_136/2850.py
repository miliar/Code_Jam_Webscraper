import sys

def build(C, F, X, G):
    elapsed = 0.0
    tm_min = X / G
    for i in xrange(int(X/C) + 1):
        tm_nb = elapsed + X / G
        if tm_nb < tm_min:
            tm_min = tm_nb
        elapsed += C / G
        G += F
    return tm_min

def solve(C, F, X):
    return build(C, F, X, 2.0)

def main():
    line_num = int(raw_input())
    for i in xrange(line_num):
        line = raw_input()
        C, F, X = map(float, line.split(' '))
        res = solve(C, F, X)
        print 'Case #%d: %.7f' % (i+1, res)

main()
