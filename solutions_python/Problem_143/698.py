#-------------------------------------------------------------------------------
# Name:        New Lottery Game
# Purpose:
#
# Author:      nikos912000
#
# Created:     03/05/2014
# Copyright:   (c) nikos912000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sol(A, B, K):

    cnt = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                cnt += 1
    return cnt

def main():
    f = open('B-small-attempt0.in')
    g = open('output','w')

    T = int(f.readline())

    for case in range(1,T + 1):
        A, B, K = map(int,f.readline().split())
        res = sol(A,B,K)
        g.write('Case #%d: %d\n' %(case,res))

if __name__ == '__main__':
    main()
