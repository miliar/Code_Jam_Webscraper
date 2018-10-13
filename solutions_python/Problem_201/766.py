from heapq import heappush, heappop

ret = []
with open('C-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        n, k = map(int, file.readline().split())

        # large solution
        userTotal = 0
        Q = []
        heappush(Q, (-n, 1))
        lastmin = None
        lastmax = None
        while userTotal < k:
            x, available = heappop(Q)
            if Q:
                while Q[0][0] == x:
                    x, more = heappop(Q)
                    available += more
                    if not Q: break
            userTotal += available
            x *= -1
            x -= 1
            lastmin = x//2
            lastmax = x-x//2
            heappush(Q, (-lastmin, available))
            heappush(Q, (-lastmax, available))
        ret.append(' '.join(map(str, (lastmax, lastmin))))


with open('Cout_large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))

