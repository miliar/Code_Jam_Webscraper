#!/usr/bin/env python2
def solve(x):
    while x != int(''.join(sorted(str(x)))):
        x -= 1
    return x
def solve2(ns):
    ns = str(ns)
    ns = map(int, ns)
    i = 0
    while True:
        j = i
        while j + 1 < len(ns):
            j += 1
            if ns[j] == ns[i]:
                continue
            elif ns[j] > ns[i]:
                i = j
                break
            else:
                ns[i] -= 1
                ns[i+1:] = [9 for _ in ns[i+1:]]
                break
        else:
            break
    ns = int(''.join(map(str, ns)))
    return ns
for t in xrange(1, 1 + int(raw_input())):
    print 'Case #%d:' % t,
    ns = int(raw_input().strip())
    ns = solve2(ns)
    print ns
