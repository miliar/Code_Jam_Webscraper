#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

MOD = 1000002013

def cost(N, dist, discount):
    return dist * (N-discount) - (dist-1)*dist/2

def main():
    T = int(sys.stdin.readline().strip())
    for t in xrange(1, T+1):
        N, M = map(int, sys.stdin.readline().strip().split())
        events = []
        actual_cost = 0
        for i in xrange(M):
            o, e, p = map(int, sys.stdin.readline().strip().split())
            events.append((o, -p))
            events.append((e, p))
            actual_cost += cost(N, e-o, 0) * p
            actual_cost %= MOD
        events.sort()
        cur = []
        min_cost = 0
        old_pos = 0
        for ev in events:
            old_cur = cur
            cur = []
            cur_pos = ev[0]
            if cur_pos == old_pos:
                cur = old_cur
            else:
                for discount, n in old_cur:
                    if n:
                        min_cost += cost(N, cur_pos - old_pos, discount) * n
                        min_cost %= MOD
                        cur.append((discount + cur_pos-old_pos, n))
            old_pos = cur_pos

            if ev[1] < 0:
                cur = [(0, -ev[1])] + cur
            else:
                p = ev[1]
                for i in xrange(len(cur)):
                    if cur[i][1] >= p:
                        cur[i] = (cur[i][0], cur[i][1] - p)
                        break
                    else:
                        p -= cur[i][1]
                        cur[i] = (cur[i][0], 0)

        print "Case #" + str(t) + ":", (actual_cost + MOD - min_cost) % MOD


if __name__ == '__main__':
    main()
