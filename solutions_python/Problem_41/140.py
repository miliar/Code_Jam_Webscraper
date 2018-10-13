#!/usr/bin/python

import sys
from itertools import islice

def read_tests(file):
    T = int(list(islice(file, 1))[0])
    for N_str in file:
        yield int(N_str)

def get_smallest(tail, head):
    avail = [(el,i) for i, el in enumerate(tail) if el > head]
    if avail:
        return min(avail)[1]
    else:
        return None

def solve(N):
    Nd = map(int, list(str(N)))
    for dist in range(2, len(Nd)+1):
        tail = Nd[-dist:]
        head = tail.pop(0)
        repl_idx = get_smallest(tail, head)
        if repl_idx != None:
            return int(''.join(map(str, Nd[:-dist] + [tail.pop(repl_idx)] + sorted(tail+[head]))))

    res = sorted(Nd)
    res.insert(1, 0)
    repl_idx2 = None
    for i, el in enumerate(res):
        if el != 0:
            repl_idx2 = i
            break
    if repl_idx2 != None:
        res = [res.pop(repl_idx2)] + res
    res = int(''.join(map(str, res)))
    if res < N:
        raise Exception("%d < %d" % (res, N))
    elif res == N:
        return res*10
    else:
        return res

if __name__ == '__main__':
    for i, test in enumerate(read_tests(open(sys.argv[1]))):
        print "Case #%d: %d" % (i+1, solve(test))
