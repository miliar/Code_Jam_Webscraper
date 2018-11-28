from heapq import heappush as push, heappop as pop, heappushpop as pushpop
for t in xrange(input()):
    n, k = map(int, raw_input().split())
    s, c = [-n], {-n: 1}
    print "Case #" + str(t+1) + ":",
    
    while k > c[s[0]]:
        k -= c[s[0]]
        if s[0] % 2:
            if s[0]/2+1 in c:
                c[s[0]/2 + 1] += c[s[0]]*2
                del c[s[0]]
                pop(s)
            else:
                c[s[0]/2 + 1] = c[s[0]]*2
                del c[s[0]]
                pushpop(s, s[0]/2 + 1)
        else:
            if s[0]/2+1 in c:
                c[s[0]/2 + 1] += c[s[0]]
            else:
                c[s[0]/2 + 1] = c[s[0]]
                push(s, s[0]/2 + 1)
            if s[0]/2 in c:
                c[s[0]/2] += c[s[0]]
                del c[s[0]]
                pop(s)
            else:
                c[s[0]/2] = c[s[0]]
                del c[s[0]]
                pushpop(s, s[0]/2)
    
    print -s[0]/2, (-s[0]-1)/2