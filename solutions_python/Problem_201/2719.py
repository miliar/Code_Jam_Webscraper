import fileinput
f = fileinput.input()
import heapq
import sys
t = input()
c = 0
printflag = 0
while t:
    c += 1
    t-=1
    [n,k] = map(int, raw_input().split())
    pq = [[-n,0,n-1]]
    a,b = -1,-1
    while k:
        k -= 1
        [l,s,e] = heapq.heappop(pq)
        l = -l
        #print l,s,e
        if l%2==0:
            if l>2:
                a = max([l/2-1,l/2])
                b = min([l/2-1,l/2])
                heapq.heappush(pq,[-(l/2-1), s, s+l/2-1])
                heapq.heappush(pq,[-(l/2), s+l/2,e])
            else:
                a = 1
                b = 0
                heapq.heappush(pq,[-1, e, e])
        else:
            if l>2:
                a = l/2
                b = l/2
                heapq.heappush(pq,[-(l/2), s,s+l/2-1])
                heapq.heappush(pq,[-(l/2), s+l/2+1, e])
            else:
                a = 0
                b = 0

    res = "Case #"+str(c)+": "+str(a)+" "+str(b)
    if printflag != 0:
        sys.stdout.write("\n")
    else:
        printflag = 1
    sys.stdout.write(res)
    

    
    
