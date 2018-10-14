import heapq
f = open("C-small-2-attempt6.in","r")
number = int(f.readline())
def stall(n,k):

    def first(x):
        return x/2
    def second(x):
        return x-1-x/2
    if n == k:
        return "0 0"
    q = [-n]
    if k == 1:
        return str(first(n))+" "+str(second(n))
    for i in range(k-1):
        a = -heapq.heappop(q)
        if a == 1:
            return "0 0"
        heapq.heappush(q,-(first(a)))
        heapq.heappush(q,-second(a))
    a = -heapq.heappop(q)
    return str(first(a))+" "+str(second(a))
for i in range(number):
    s= f.readline()
    s = s.split()
    n = int(s[0])
    k = int(s[1])
    print("Case #"+str(i+1)+": "+stall(n, k))



