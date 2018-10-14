#!/usr/bin/env python

import sys

class Snapper:
    
    def __init__(self, state, has_power):
        self.state = state
        self.has_power = has_power
    def __repr__(self):
        return "<State:%s Power:%s>" % (self.state, self.has_power)

def print_solution(answer, case):
    print "Case #%d: %s" % (case, answer)

def solve(N, K, case):
    snappers = [Snapper(False, False) for i in range(N)]
    snappers[0].has_power = True
    
    for i in range(K):
        was_on = True
        for i, s in enumerate(snappers):
            if was_on:
                if s.state:
                    s.state = False
                else:
                    s.state = True
                    was_on = False
    if all(s.state for s in snappers):
        print_solution('ON', case)
    else:
        print_solution('OFF', case)

def main():
    cases = []
    T = int(sys.stdin.readline())
    for i in range(1, T + 1):
        N, K = sys.stdin.readline().strip().split(' ')
        solve(int(N), int(K), i)

if __name__ == '__main__':
    main()

