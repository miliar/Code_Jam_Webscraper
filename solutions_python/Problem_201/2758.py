from heapq import *

def printResult(maxi, mini, number):
    print('Case #{}: {} {}'.format(number, maxi, mini))

for tc in range(int(input().strip())):
    n, k = [int(x) for x in input().strip().split()]
    maxHeap = []
    heappush(maxHeap, n * -1)
    for i in range(k):
        longest = heappop(maxHeap) * -1
        if longest == 0:
            Ls = 0
            Rs = 0
        else:
            Ls = int((longest - 1) / 2)
            Rs = longest - 1 - Ls
        heappush(maxHeap, Ls * -1)
        heappush(maxHeap, Rs * -1)
        if i == k - 1:
            printResult(max(Ls, Rs), min(Ls, Rs), tc+1)








