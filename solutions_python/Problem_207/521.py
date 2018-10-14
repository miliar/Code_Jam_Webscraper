
import collections
import heapq


class Sentinel:
    pass


def d_e(lst):
    counts = collections.Counter(lst)
    heap = [(-count, key) for key, count in counts.items()]
    heapq.heapify(heap)
    output = []
    last = Sentinel()
    while heap:
        minuscount1, key1 = heapq.heappop(heap)
        if key1 != last or not heap:
            last = key1
            minuscount1 += 1
        else:
            minuscount2, key2 = heapq.heappop(heap)
            last = key2
            minuscount2 += 1
            if minuscount2 != 0:
                heapq.heappush(heap, (minuscount2, key2))
        output.append(last)
        if minuscount1 != 0:
            heapq.heappush(heap, (minuscount1, key1))
    return output


file = open("B.in")
out  = open("bans.txt", "w")

input = file.readline
print = out.write

def tr(n):
    for i in range(len(n)-1):
        if n[i] == n[i+1] or n[i] == n[i-1]:
            return False
    return True

def com(r, y, b):
    new = []
    for i in range(r):
        new.append('R')
    for i in range(y):
        new.append('Y')
    for i in range(b):
        new.append('B')
    for i in range(g):
        new.append('G')
    for i in range(o):
        new.append('O')
    for i in range(v):
        new.append('V')
    new = d_e(new)
    le = len(new)
    if new[0] == new[le-1]:
        new[le-2], new[le-1] = new[le-1], new[le-2]
    return new
    
    

T = int(input())
for t in range(T):
    N, r, o, y, g, b, v = map(int, input().split(' '))
    col = [r, o, y, g, b, v]
    true = True
    for c in col:
        if c > N/2:
            ans = 'IMPOSSIBLE'
            true = False
    if true:
        ans = ''
        A = com(r, y, b)
        for a in A:
            ans += a
    print("Case #{}: {}\n".format(t+1, ans))
