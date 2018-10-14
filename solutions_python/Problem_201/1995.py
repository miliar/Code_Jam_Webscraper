#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    N, K = map(int, cipher.split())
    L = range(N)
    R = range(N-1, -1, -1)
    for k in range(K):
        mins = {}
        maxes = {}
        for i in range(N):
            if L[i] is None or R[i] is None:
                continue
            if min(L[i], R[i]) not in mins:
                mins[min(L[i], R[i])] = []
            mins[min(L[i], R[i])].append(i)
        candidate_stalls = mins[max(mins)]
        if len(candidate_stalls) > 1:
            for i in candidate_stalls:
                if max(L[i], R[i]) not in maxes:
                    maxes[max(L[i], R[i])] = []
                maxes[max(L[i], R[i])].append(i)
            candidate_stalls = maxes[max(maxes)]
        selected_stall = min(candidate_stalls)
        L[selected_stall] = None
        R[selected_stall] = None
        count = 0
        for i in range(selected_stall-1, -1, -1):
            if R[i] is None:
                break
            R[i] = count
            count += 1
        count = 0
        for i in range(selected_stall+1, len(L)):
            if L[i] is None:
                break
            L[i] = count
            count += 1
        if k == K-1:
            to_right = 0
            to_left = 0
            i = 1
            while selected_stall+i < len(R) and R[selected_stall+i] is not None:
                to_right += 1
                i += 1
            i = -1
            while selected_stall+i >= 0 and L[selected_stall+i] is not None:
                to_left += 1
                i -= 1
            return '%s %s' % (max(to_left, to_right), min(to_left, to_right))


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
