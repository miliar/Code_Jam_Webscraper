# python2
import sys
import math
import heapq

class main():
    T = int(sys.stdin.readline().rstrip())
    
    for t in range(T):
        line = sys.stdin.readline().rstrip()
        temp = line.split()
        N = int(temp[0])
        K = int(temp[1])

        H = [[-N, -1]]
        heapq.heapify(H)
        #heapq.heappush(H, [-N, -1])
        
        count = 0
        while (count < K):
            [i, j] = heapq.heappop(H)
            [i, j] = [-i, -j]
            mini = (i-1) / 2
            maxi = i - 1 - mini
            
            count = count + j
            if (count >= K):
                print "Case #" + str(t+1) + ": " + str(maxi) + " " + str(mini)
            else:
                if (mini == maxi):
                    heapq.heappush(H, [-maxi, -j*2])
                else:
                    heapq.heappush(H, [-maxi, -j])
                    heapq.heappush(H, [-mini, -j])
