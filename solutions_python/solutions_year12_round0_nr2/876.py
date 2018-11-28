#! /usr/bin/python
def solve(N, S, P, ns):
    if P == 0:
        return len(ns)
    if P == 1:
        return sum(1 for i in ns if i > 0)
    total = 0
    for n in sorted(ns)[::-1]:
        if n >= (3*P-2):
            total += 1
        elif n >= (3*P-4):
            if S>0:
                total += 1
                S -= 1
        else:
            break
    return total

T = input()
for c in range(1, T+1):
    l = map(int, raw_input().split())
    print "Case #%d: %d" % (c, solve(l[0], l[1], l[2], l[3:]))
