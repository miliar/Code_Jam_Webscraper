import math

def area(r):
    return math.pi * r * r

def perim(r):
    return 2 * math.pi * r

def totalarea(rh):
    if not rh:
        return 0
    
    a = area(rh[0][0]) + perim(rh[0][0]) * rh[0][1]

    i = 1
    while i < len(rh):
        a += perim(rh[i][0]) * rh[i][1]
        i += 1
    return a

def delpan(rh):
    maxa = 0
    maxi = 0
    i = 0
    arearh = totalarea(rh)
    while i < len(rh):
        if (i == 0 and len(rh) > 1):
            ar = arearh - perim(rh[0][0]) * rh[0][1]
            ar = ar - (area(rh[0][0]) - area(rh[1][0]))
        else:
            ar = arearh - perim(rh[i][0]) * rh[i][1]
        
        if ar > maxa:
            maxa = ar
            maxi = i

        i += 1
    rh.pop(maxi)
    return rh

fi = open('A-large.in', 'r')
fo = open('outputA-large.txt', 'w')

T = int(fi.readline())

for t in range(1, T+1):
    
    linetok = fi.readline().split()
    n = int(linetok[0])
    k = int(linetok[1])

    rh = [(0, 0)] * n

    for i in range(n):
        linetok = fi.readline().split()
        rh[i] = (int(linetok[0]), int(linetok[1]))

    rh = sorted(rh, key= lambda rh: rh[0])
    rh = list(reversed(rh))

    pantodel = n - k

    d = 0
    while d < pantodel:
        rh = delpan(rh)
        d += 1

    fo.write('Case #{}: {}\n'.format(t, totalarea(rh)))
    
fi.close()
fo.close()
