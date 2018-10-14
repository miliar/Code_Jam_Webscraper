#!/usr/bin/python
import sys
basename, = sys.argv[1:]
input_filename = basename + ".in"
output_filename = basename + ".out"
input = open(input_filename)
output = open(output_filename, 'w')
print 'writing to', output_filename

T = int(input.readline())

def f(P, target, n, offsets):
#    print "f", P, target, n, offsets
    ## conteggi e probabilita' di avere count occorrenze della parola
    ## target oppure delle parole offsets all'inizio
    count0 = len([x for x in offsets if x==''])
    if n == 0:
        return {count0: 1.0}
    pbs = {}  ## count -> pb
    for c in P:
        o2 = [x[1:] for x in offsets if x and x[0] == c]
        if target[0] == c:
            o2.append(target[1:])
        ppbs = f(P, target, n-1, o2)
        for count, p in ppbs.items():
            co = count + count0
            if not co in pbs:
                pbs[co] = 0.0
            pbs[co] += P[c] * p
    return pbs
            
def solve():
    K, L, S = map(int, input.readline().strip().split())
    cars = input.readline().strip()
    assert len(cars) == K
    target = input.readline().strip()
    assert len(target) == L
    P = {}
    for c in cars:
        if c in P:
            P[c] += 1
        else:
            P[c] = 1
    n = float(K)
    P = {c: k/n for c, k in P.items()}
    pbs = f(P, target, S, [])
    m = max(pbs.keys())
    a = sum([ n*p for (n,p) in pbs.items()])
    print K, L, S, '->', m-a
    return m-a
        
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
