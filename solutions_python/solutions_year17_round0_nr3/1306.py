__author__ = 'rutger'
import queue

def split(n):
    return n//2, n//2 -1 + (n%2)

def solve2(n, k):
    stallsTaken = 0
    lastMax = 0
    lastMin = 0
    a = [(n, 1)]
    while stallsTaken < k:
        lastMax, lastMin = split(a[0][0])
        amount = a[0][1]
        stallsTaken += amount
        a = a[1:]
        a.append((lastMax, amount))
        a.append((lastMin, amount))
        a = sorted(a, reverse=True)
    return lastMax, lastMin

def solve(n, k):
    stallsTaken = 0
    lastMax = 0
    lastMin = 0
    amounts = {}
    q = queue.PriorityQueue()
    q.put(-n)
    amounts[n] = 1
    while stallsTaken < k:
        top = abs(q.get())
        amount = amounts.get(top)

        #print('stalls %d' % stallsTaken)
        #print('top %d    amount %d' % (top, amount))

        lastMax, lastMin = split(top)
        stallsTaken += amount

        if amounts.get(lastMax, -1) == -1:
            q.put(-lastMax)
        amounts[lastMax] = amounts.get(lastMax, 0) + amount
        if amounts.get(lastMin, -1) == -1:
            q.put(-lastMin)
        amounts[lastMin] = amounts.get(lastMin, 0) + amount

        amounts[n] = 0
        #print(amounts)
    return lastMax, lastMin


for T in range(int(input())):
    n, k = list(map(int, input().split(' ')))

    maximum, minimum = solve(n, k)
    print('Case #%d: %d %d' % (T + 1, maximum, minimum))

