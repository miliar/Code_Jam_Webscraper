import sys

def num_intersections(As, Bs):
    
    count = 0
    #print As, Bs
    
    for i in range(N):
        for j in range(i+1, N):
            #print i, j
            if (As[i] > As[j] and Bs[i] < Bs[j]) or (As[i] < As[j] and Bs[i] > Bs[j]):
                count += 1
    
    return count


if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        N = int(sys.stdin.readline())
        As = []
        Bs = []
        for j in range(N):
            A, B = map(int, sys.stdin.readline().strip().split())
            As.append(A)
            Bs.append(B)
        ans = num_intersections(As, Bs)
        print 'Case #%s: %s' %  (i, ans)
