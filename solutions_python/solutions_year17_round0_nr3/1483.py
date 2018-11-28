#!/usr/bin/python
import heapq
def Bathroom():
    T = int(raw_input())
    for i in xrange(1,T+1):
        N,K = map(int, raw_input().split() )
        #print N, K
        y,z = stall(N, K)
        print "Case #"+ str(i)+ ":",
        print y, z

def stall(N,K):
    #l = [(1,N)]
    h = []
    heapq.heappush(h, (-N, (1, N)) )
    if N == K: return 0,0
    for i in xrange(K):
        # print h , "start finding"
        y, z = find(h)
        # print i, h, "finishing finding h"

    return y,z

def find(h):

    # print h
    bggst_space =  heapq.heappop(h)

    # print "finding h:", len(bggst_space), bggst_space
    start, end, nspace = bggst_space[1][0], bggst_space[1][1], bggst_space[0]
    space = - nspace
    if space == 2:
        heapq.heappush(h, (-1, (end, end) ))
        left,right =  (1,0)
    elif space == 1:
        left,right = (0,0)
    elif space > 2:
        if space % 2 == 0:
            m = space/2 + start -1
            left,right =  (space/2, space/2-1)
        else:
            m = (space-1)/2 + start 
            left,right =  ((space-1)/2, (space-1)/2)
        heapq.heappush(h, ( -(m-1-start+1), (start, m-1) )  )

        heapq.heappush(h, (-(end - (m+1) + 1 ), (m+1, end) ) )

    else: 
        print 'something wrong'

    return left,right



if __name__ == "__main__":
    Bathroom()




