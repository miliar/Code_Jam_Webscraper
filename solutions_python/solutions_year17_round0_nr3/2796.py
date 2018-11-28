import sys
import heapq

def place(n, k):
#    print "n:{}, k:{}".format(n, k)
    s = [-n]
    for i in range(k):
        d = -heapq.heappop(s)
        if d % 2 == 0:
            max_gap = d / 2
            min_gap = max(d / 2 - 1, 0)
        else:
            max_gap = min_gap = d / 2
#        print max_gap, min_gap
        heapq.heappush(s, -max_gap)
        heapq.heappush(s, -min_gap)
    return (max_gap, min_gap)
        
        

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(1,t+1):
        l = sys.stdin.readline().split(' ')
        n = int(l[0])
        k = int(l[1])
        (max_gap, min_gap) = place(n, k)
        print 'Case #{}: {} {}'.format(i, max_gap, min_gap)

        
