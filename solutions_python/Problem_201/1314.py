import sys
from queue import PriorityQueue

def bathroom(N,K):
    q = PriorityQueue()
    q.put(-N)
    for i in range(K):
        x = -q.get()
        x -=1

        mi = x//2
        ma = mi + (x%2)
        #print ("%d %d (%d,%d)" % (i+1, x, ma, mi))
        q.put(-ma)
        q.put(-mi)

    return (ma,mi)

if __name__=='__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        (N,K) = sys.stdin.readline().split(' ')
        (ma, mi) = bathroom(int(N),int(K))
        print("Case #%d: %d %d" % (i+1, ma, mi))

