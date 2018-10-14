import itertools

def dec(n, start, stop):
    i = stop
    while i >= 0:
        if n[i] > 0:
            n[i] -= 1
            if i > 0 and n[i - 1] > n[i]:
                fix(n, start, i - 1, stop)
            return
        else:
            n[i] = 9
            i -= 1

def nines(n, start, stop):
    n[start:stop + 1] = [9] * (stop - start + 1)

def fix(n, start, cut, stop):
    dec(n, start, cut)
    nines(n, cut + 1, stop)

def find_cut(n):
    for i in xrange(len(n) - 1):
        if n[i] > n[i + 1]:
            return i
    return None

def tidy(n):
    n = [int(i) for i in n]
    cut = find_cut(n)
    if cut is not None:
        fix(n, 0, cut, len(n) - 1)
    nozeros = itertools.dropwhile(lambda x: x == 0, n)
    return "".join(str(i) for i in nozeros)

for t in xrange(input()):
    print "Case #%d: %s" % (t + 1, tidy(raw_input()))



