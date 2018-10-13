#!/usr/bin/env python

def permute(seq):
    if len(seq) <=1:
        yield seq
    else:
        for perm in permute(seq[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + seq[0:1] + perm[i:]

def simulate_release(prisoners, order):
    cost = 0
    ps = [i for i in prisoners]
    for p in order:
        ps[p - 1] = 0
        for l in ps[p:]:
            if l == 1:
                cost += 1
            else:
                break
        for l in reversed(ps[:p-1]):
            if l == 1:
                cost += 1
            else:
                break
    return cost

def solve(P, released):
    prisoners = [1 for i in range(P)]
    min_bribe = simulate_release(prisoners, released)
    for perm in permute(released):
        bribe = simulate_release(prisoners, perm)
        if bribe < min_bribe:
            min_bribe = bribe
    return min_bribe

def main():
    N = int(raw_input())
    for count in range(N):
        P, Q = [int(s) for s in raw_input().split()]
        released = [int(s) for s in raw_input().split()]
        answer = solve(P, released)
        print 'Case #%d: %d' % (count + 1, answer)

if __name__ == '__main__':
    main()

