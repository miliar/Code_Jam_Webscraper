import heapq
T = int(raw_input())
for t in xrange(T):
    N, K = map(int, raw_input().split())

    d = dict()
    d[N] = 1
    
    h = [] 
    heapq.heappush(h, -N)

    k = K
    while (True):
        next_num = -heapq.heappop(h)
        next_cnt = d[next_num]
        # print next_num, next_cnt

        if next_cnt >= k:
            break
        
        k -= next_cnt
        
        if next_num % 2 == 0:
            c = next_num / 2
            if not c in d: 
                d[c] = 0
                heapq.heappush(h, -c)
            d[c] += next_cnt
            if not c-1 in d: 
                d[c-1] = 0
                heapq.heappush(h, -c+1)
            d[c-1] += next_cnt

        elif next_num % 2 == 1:
            c = next_num / 2
            if not c in d: 
                d[c] = 0
                heapq.heappush(h, -c)
            d[c] += next_cnt * 2

         

    base = next_num
    if base % 2 == 0:
        print 'Case #%d: %d %d' % (t+1, base/2, base/2-1)
    else:
        print 'Case #%d: %d %d' % (t+1, base/2, base/2)


        
        




