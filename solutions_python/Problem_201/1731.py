import math
import sys
import os


def enter(stalls, L, R, n):

    choice = 10000000
    best_min = -1
    best_max = -1
    
    for i in xrange(n):
        if stalls[i]:
            continue

        curr_min = min(L[i], R[i])
        curr_max = max(L[i], R[i])
        
        if curr_min > best_min:
            best_min = curr_min
            best_max = curr_max
            choice = i
        elif curr_min == best_min and curr_max > best_max:
            best_max = curr_max
            choice = i            

    stalls[choice] = True

    i = choice - 1
    while i >= 0:
        R[i] = choice - i - 1
        if stalls[i]:
            break
        i -= 1

    i = choice + 1
    while i < n:
        L[i] = i - choice - 1
        if stalls[i]:
            break
        i += 1

    return choice
        

def func(i):

    n, k = map(int, sys.stdin.readline().split())

    choice = -1

    stalls = [False] * n
    L = [i for i in xrange(n)]
    R = L[-1::-1]

    for i in xrange(k):
        choice = enter(stalls, L, R, n)
        # print stalls, L, R

    best_min, best_max = min(L[choice], R[choice]), max(L[choice], R[choice])
        
    return "{0} {1}".format(best_max, best_min)



def inp(t):

    for i in xrange(1, t + 1):
        ans = func(i)
        print "Case #{0}: {1}".format(i, ans)

    return


def main(argv):

    t = int(sys.stdin.readline())

    inp(t)

    return


if __name__ == "__main__":
    main(sys.argv)
