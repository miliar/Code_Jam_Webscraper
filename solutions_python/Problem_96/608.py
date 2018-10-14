#!/usr/bin/python

def solve():
    ins = map(int, raw_input().split(' '))
    special = ins[1]
    p = ins[2]
    ns = ins[3:]
    result = 0
    for n in ns:
        base, m = divmod(n, 3)
        if m > 0:
            base += 1
        if base >= p:
            result += 1
        elif special > 0 and ((m == 0 and base > 0) or (m == 2)) and base + 1 >= p:
            result += 1
            special -= 1
    return result

if __name__ == '__main__':
    T = int(raw_input())
    for case in xrange(1, T+1):
        print "Case #{0}: {1}".format(case, solve())
