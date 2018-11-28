import Queue

def clean(a):
    clean = []
    for i in xrange(len(a)):
        if a[i] > 0:
            clean.append(a[i])
    return clean

def normal(a):
    a = [i - 1 for i in a]
    return clean(a)

def special(a, i, j):
    new = a[:]
    new[i] -= j
    new.append(j)
    return clean(new)

def analysis():
    no_diners = int(raw_input())
    diners = map(int, raw_input().split())

    store = (diners, 0)
    q = Queue.Queue()
    q.put(store)
    added = set()
    low = []
    while not q.empty():
        elem = q.get()
        if elem[0] == []:
            low.append(elem[1])
        a = normal(elem[0])
        asort = tuple(sorted(a))
        if asort not in added:
            q.put((normal(elem[0]), elem[1] + 1))
            added.add(asort)
        for i in xrange(len(elem[0])):
            for j in xrange(2, (elem[0][i] / 2) + 1):
                b = special(elem[0], i, j)
                bsort = tuple(sorted(b))
                if bsort not in added:
                    q.put((b, elem[1] + 1))
                    added.add(bsort)

    return min(low)

cases = int(raw_input())

for i in xrange(cases):
    output = "Case #%i: %i" % (i+1, analysis())
    print output
