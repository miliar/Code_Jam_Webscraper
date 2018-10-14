fi = open('A-large.in', 'r')
fo = open('outputA-large.txt', 'w')

T = int(fi.readline())

for t in range(T):

    linetok = fi.readline().split()
    d = int(linetok[0])
    n = int(linetok[1])
    tmax = 0
    for i in range(n):
        linetok2 = fi.readline().split()
        ki = int(linetok2[0])
        si = int(linetok2[1])
        tp = (d - ki) / si
        if tp > tmax:
            tmax = tp

    fo.write('Case #{0}: {1:.6f}\n'.format(t+1, d / tmax))
    
fi.close()
fo.close()
