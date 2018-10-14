import fileinput
import math
import sys
    

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in xrange(T):
        A, N = map(int, sys.stdin.readline().split(' '))
        l = map(int, sys.stdin.readline().split(' '))
        if A == 1:
            ans = N
            print "Case #{}: {}".format(i+1, int(ans))
            continue
        l.sort()
        #print A, N, l
        minops = float('inf')
        counter = 0
        j = 0
        while j < N:
            item = l[j]
            #print A, counter, item
            if item < A:
                A += item
                j += 1
                continue
            minops = min(minops, N-j+counter)
            A += A-1
            counter += 1
        ans = min(counter, minops)

        print "Case #{}: {}".format(i+1, int(ans))
