from collections import Counter

def Solver(N,K):

    r=set([])
    q = Counter()
    q[N] += 1
    r.add(N)

    for i in range(K):

        most = max(r)

        q[most] -=1

        if q[most]<1:
            r.remove(most)

        l = (most-1)/2
        m = most- 1 -l

        q[l] += 1
        q[m] += 1

        r.add(l)
        r.add(m)

    return m,l

import sys

def main():

    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in xrange(nums):
            N,K = f.readline().strip().split()
            N,K = int(N),int(K)

            m,l = Solver(N,K)
            print "Case #{:d}: ".format(i+1)+str(m) +' '+str(l)

main()
