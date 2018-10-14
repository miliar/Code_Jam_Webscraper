#contest 170201
import math
import collections
import heapq
import string

def problem_A(N, K):
    ocp = set([0,N+1])
    status = [(0,0) for _ in xrange(N+2)]
    status_dist = [(0,0) for _ in xrange(N+2)]

    def update():
        l,r = 0,0
        for i in xrange(len(status)):
            if i in ocp:
                l = -1
            status[i] = (l, status[i][1])
            l += 1
        for j in xrange(len(status)-1, -1, -1):
            if j in ocp:
                r = -1
            status[j] = (status[j][0],r)
            status_dist[j] = (min(status[j]),max(status[j]))
            r += 1

    for i in xrange(K):
        update()
        mind, maxd  = 0, 0
        index = 0
        for j, v in enumerate(status_dist):
            if v[0] > mind:
                index = j
                mind, maxd = v[0], v[1]
            elif v[0] == mind and v[1] > maxd:
                index = j
                maxd = v[1]
        ocp.add(index)

    return maxd, mind


def problem_B(n):
    size = len(str(n))
    if int('1'*size) > n:
        size -= 1

    top = 1
    str_int = {v:i for i,v in enumerate('0123456789')}
    int_str = {i:v for i,v in enumerate('0123456789')}
    # tidy_stack = []
    tidy_str = ''
    for i in xrange(size,0,-1):
        while top<9 and int(tidy_str+int_str[top+1]*i) <= n:
            top += 1
        tidy_str += int_str[top]
    return tidy_str

def main_B():
    T = int(raw_input())
    for i in xrange(1,T+1):
        n = int(raw_input())
        sol = problem_B(n)
        print "Case #{}: {}".format(i, sol)

def main_A():
    T = int(raw_input())
    for i in xrange(1,T+1):
        N, K = [int(_) for _ in raw_input().split()]
        y, z = problem_A(N, K)
        print "Case #{}: {} {}".format(i, y, z)

if __name__=='__main__':
    main_A()