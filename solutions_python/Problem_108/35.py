#!/usr/bin/python

def solve(vines, dest):
    memo = {}

    def inner(start_pos, grabbed_pos):
        r = memo.get((start_pos, grabbed_pos))
        if r is not None:
            return r
        low = start_pos
        high = grabbed_pos + (grabbed_pos - start_pos)
        if dest <= high:
            return True
        for d, l in vines:
            if low < d <= high:
                new_start = max(grabbed_pos, d - l)
                #reachable
                if inner(new_start, d):
                    memo[(start_pos, grabbed_pos)] = True
                    return True
        memo[(start_pos, grabbed_pos)] = False
        return False

    return inner(0, vines[0][0])

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    vines = []
    for j in range(N):
        vines.append(tuple(map(int, raw_input().split())))
    print "Case #%i: %s" % (i+1, 'YES' if solve(vines, int(raw_input())) else 'NO')
