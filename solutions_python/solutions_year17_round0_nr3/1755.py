import heapq

def findMinMax(p,n):
    h = []
    heapq.heappush(h,-1*p)
    '''
    if p % 2 == 0:
        if p//2 == n:
            return "1 0"
        elif p//2 < n:
            return "0 0"
    else:
        if (p-1)//2 % 2 == 1:
            if (p-1)//2 == n:
                return "1 0"
            elif (p-1)//2 < n:
                return "0 0"
        else:
            if (p-1)//2 == n:
                return "1 1"
            elif (p-1)//2 < n:
                return "0 0"
     '''          
    for i in range(n):
        biggest = heapq.heappop(h)*-1
        one = biggest//2 
        two = biggest - one - 1
        heapq.heappush(h,one*-1)
        heapq.heappush(h,two*-1)
        if one == 0 and two == 0:
            return "0 0"
    return str(one) + " " + str(two)
        
l = int(raw_input())
for x in range(l):
    p,n = map(int,raw_input().split())
    print "Case #"+str(x+1)+": "+ findMinMax(p,n)
    