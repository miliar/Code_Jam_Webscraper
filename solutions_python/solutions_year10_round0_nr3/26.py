
if __name__ == '__main__':
    fin = 'C-small.in'
    fon = 'C-small.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        r,k,_ = [int(x) for x in fi.readline().split(' ')]
        gs = [int(x) for x in fi.readline().split(' ')]
        n = len(gs)
        
        # the cost of trip start at nth group is hist[n]
        hist = [0]*n
        
        # if the trip starts at nth group, next trip start at next[n]th gruop
        next = [-1]*n
        
        for p in xrange(n):
            t = 0
            lt = t
            nx = -1
            for q in xrange(n):
                lt = t
                t = t + gs[(p + q) % n]
                if t > k:
                    hist[p] = lt
                    next[p] = (p + q) % n
                    break
            if t <= k:
                hist[p] = t
                next[p] = p
                
        #print 'grou:',gs
        #print 'hist:',hist
        #print 'next:',next
        
        # find start of the loop
        # loop is sure to be found
        visited = [False]*n
        pos = 0
        loop_begin = -1        
        for p in xrange(n):
            visited[pos] = True
            pos = next[pos]
            if visited[pos]:
                loop_begin = pos
        
        # count the cost of each loop and its length
        pos = loop_begin
        loop_cost = [0]*n
        loop_len = 0
        for _ in xrange(n):
            loop_cost[pos] += 1
            pos = next[pos]
            loop_len += 1
            if pos == loop_begin:
                break
        
        #print 'loop_begin:',loop_begin
        #print 'loop_len',loop_len
        #print 'loop_cost',loop_cost
                
        # calculate the cost until loop_begin is found
        count = [0]*n
        pos = 0
        while r != 0:
            count[pos] += 1
            pos = next[pos]
            r -= 1
            if pos == loop_begin:
                break;
        
        if r != 0:
            #print 'left:',r
            
            # calculate cost during repetitious loops
            loop_count = r/loop_len
            r = r % loop_len
            
            #print 'left mod:',r
            #print 'loop_count:',loop_count
            
            for p in xrange(n):
                count[p] += loop_count * loop_cost[p] 
            
            # continue calculating the cost, normal way
            while r != 0:
                count[pos] += 1
                pos = next[pos]
                r -= 1
                         
        ans = sum(count[x]*hist[x] for x in xrange(n))
        
        fo.write("Case #%d: %d\n" % (i + 1, ans))
    
    print "Done!"
    fi.close()
    fo.close()

