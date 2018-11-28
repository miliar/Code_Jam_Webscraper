
from heapq import heappush, heappop, _heapify_max, heapify

def Solve(n, k):
    heap = []
    heappush(heap, -n)
    first, second = 0,0
    for i in range(0,k):
        a = heappop(heap)
        if a < -1:
            if (a%2):
                heappush(heap, int(a/2))
                heappush(heap, int(a/2))
            else:
                heappush(heap, int(a / 2) + 1)
                heappush(heap, int(a / 2))
    a = -a
    if (a == 0):
        return 0,0
    a = a - 1
    if (a % 2):
        first = int(a/2)
        second = int(a/2) + 1
    else:
        first = int(a/2)
        second = int(a/2)
    return first, second


input = open('task3.in','r')
output = open('output3.txt','w+')
T = int(input.readline())
for t in range(T):
    n, k = input.readline().split()
    n = int(n)
    k = int(k)
    a, b = Solve(n,k)
    output.write("Case #{}: {} {}\n".format(t + 1, b, a))