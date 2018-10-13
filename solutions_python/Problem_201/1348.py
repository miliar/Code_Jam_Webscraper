import sys
import math
import heapq

def split(a):
    if (a % 2 == 0):
        return ((a/2) - 1, a/2)
    else:
        return ((a - 1)/2, (a - 1)/2)

def extractMax(h):
    (size, mult) = heapq.heappop(h)
    return (-size, mult)

def push(h, size, mult):
    heapq.heappush(h, (-size, mult))

def merge(h):
    h.sort()
    t = {}
    s = []

    for i in range(len(h)):
        (a, b) = h[i]
        if a in t:
            t[a] += b
        else:
            t[a] = b

    for (k, v) in t.iteritems():
        s.append((k, v))

    heapq.heapify(s)
    return s

def compute_min_max(n, k):
    h = []
    push(h, n, 1)

    fmax = 0
    fmin = 0

    while k > 0:
        if k % 50 == 0:
            h = merge(h)

        (size, mult) = extractMax(h)
        (l, r) = split(size)

        fmax = max(l, r)
        fmin = min(l, r)

        if l == r:
            push(h, l, 2*mult)
        else:
            push(h, l, mult)
            push(h, r, mult)

        k = k - mult

    return (fmax, fmin)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        case = 0
        for line in f:
            if case == 0:
                case += 1
                continue
            args = line.split(" ")
            n = int(args[0])
            k = int(args[1])
            (fmax, fmin) = compute_min_max(n,k)
            print "Case #%s: %s %s" % (case, fmax, fmin)
            case += 1

