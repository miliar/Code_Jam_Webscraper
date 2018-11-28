
#node = (time, prod amount, remaining)

def cmp_key(n):
    return n[0]

def shortest_time(C, F, X):
    heap = {(0.0, 2, X)}

    while len(heap) > 0:
        t, p, r = min(heap, key = cmp_key)
        heap.remove((t, p, r))

        if r == 0:
            return t

        heap.add((t + r / p, p, 0))

        if r > C:
            heap.add((t + C / p, p + F, X))

    return -1


for t in range(int(raw_input())):
    C, F, X = map(float, raw_input().split())
    print "Case #{}: {}".format(t + 1,shortest_time(C, F, X))
