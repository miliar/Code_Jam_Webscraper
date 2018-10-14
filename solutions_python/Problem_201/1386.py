import queue

def setOrAdd(_map, key, value):
    prev = 0
    if key in _map:
        prev = _map[key]
    _map[key] = prev + value

def solve(n, k):

    count = {}
    count[n] = 1

    q = queue.PriorityQueue()
    q.put((-n, n))
    indexAcc = 0
    while not q.empty():
        _, nMixed = q.get()
        n = int(nMixed)

        # Hack - item got enqueued many times
        if n not in count:
            continue

        indexAcc += count[n]
        #print (n, indexAcc, count)
        if indexAcc >= k:
            break

        m = int(n / 2)
        if n % 2 == 0:
            setOrAdd(count, m, count[n])
            setOrAdd(count, m - 1, count[n])
            q.put((-m, m))
            q.put((-(m -1), m - 1))
        else:
            setOrAdd(count, m, 2*count[n])
            q.put((-m, m))

        del count[n]

    return (int(n/2), int((n - 1)/2))

import sys
lines = sys.stdin.readlines()

for i in range(1, len(lines)):
    l = lines[i].rstrip('\n')
    n, k = l.split(' ')
    r = solve(int(n), int(k))
    print ('Case #{}: {} {}'.format(i, r[0], r[1]))
