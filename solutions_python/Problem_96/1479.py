import sys

t = int(sys.stdin.readline().rstrip())

def dodaj(n, (el,o), p):
    if el >= p: return el
    if el and n[0] > 0 and el+1 == p and o == 0:
        n[0] = n[0]-1
        return p
    if o == 2 and n[0] > 0 and el+o == p:
        n[0] = n[0]-1
        return p
    if o > 0: return el+1
    return el

for i in range(t):
    scores = map(lambda b: int(b), sys.stdin.readline().rstrip().split(' '))
    n = scores.pop(0)
    s = scores.pop(0)
    s = [s]
    p = scores.pop(0)
    best = map(lambda x: (x/3,x-(x/3)*3), scores)
    ziel = map(lambda x: dodaj(s, x, p), best)
#    print len(filter(lambda x: x >=p, ziel)), s, p, best, ziel
    print 'Case #'+str(i+1)+': '+str(len(filter(lambda x: x >=p, ziel)))


