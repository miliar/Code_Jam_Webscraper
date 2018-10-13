#!/usr/bin/python

import sys;

def main():

    T    = int(sys.stdin.readline().strip())

    for i in range(0, T):
        N     = int(sys.stdin.readline().strip())
        naomi = map(float, sys.stdin.readline().strip().split())
        ken   = map(float, sys.stdin.readline().strip().split())
        ans(N, naomi, ken, i+1)


def ans(N, naomi, ken, case):
    s_dwar = 0
    s_war  = 0

    naomi.sort()
    ken.sort()

    # calc DWar score
    for s_k in range(0, N):
        isFinish = True
        for i in range(0, N - s_k):
            if naomi[i+s_k] < ken[i]:
                isFinish = False
                break

        if isFinish:
            s_dwar = N - s_k
            break
    
    # calc War score
    i_n    = 0
    i_k    = 0
    s_k    = 0
    for i_n in range(0, N):
        while i_k < N and naomi[i_n] > ken[i_k]:
            s_war += 1
            i_k   += 1

        i_k += 1

        if i_k >= N:
            break

    #print naomi
    #print ken
    print "Case #%d: %d %d" % (case, s_dwar, s_war)


if __name__ == "__main__":
    main()

