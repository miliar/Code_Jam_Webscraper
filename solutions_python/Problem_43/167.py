#!/usr/bin/env python

def calcsecs(code):
    digitset = set(list(code))
    base = len(digitset)
    if base == 1:
        base = 2
    digitmap = dict(zip(digitset, [-1]*len(digitset)))
    leastdigit = 0

    digitmap[code[0]] = 1
    for d in code[1:]:
        if digitmap[d] == -1:
            digitmap[d] = leastdigit
            leastdigit+=1
            if leastdigit == 1:
                leastdigit = 2

    secs = 0
    power = 1

#    for d in code:
#        print digitmap[d],

    for d in reversed(code):
        secs += digitmap[d] * power
        power *= base
    return secs

def solve_case(fin):
    code = fin.readline()[:-1]
    return calcsecs(code)

def solve(fin):
    n = int(fin.readline())
    for i in range(n):
        out = solve_case(fin)
        print 'Case #{0}: {1}'.format(i+1, out)

def main():
    import sys
    solve(sys.stdin)

if __name__ == '__main__':
    main()
