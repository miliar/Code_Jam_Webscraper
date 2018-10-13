fin = open('B-small.in', 'r')
fout = open('B-small.out', 'w')
t = int(fin.readline())
def check(n, r, o, y, g, b, v, i):
    xx = {}
    if n == r + g:
        if r== g:
            return True, 'RG' * r
        else:
            return False, ''
    if n == b + o:
        if b == o:
            return True, 'BO' * b
        else:
            return False, ''
    if n == v + y:
        if v == y:
            return True, 'VY' * v
        else:
            return False, ''
    if o:
        b -= 2*o
        if b < 0:
            return False, ''
        xx['b']=[o+b, o, b, 'B', 'BOB']
    else:
        xx['b']=[b,0,b, 'B', 'BOB']

    if g:
        r -=2*g
        if r < 0:
            return False, ''
        xx['r']=[g+r, g, r, 'R', 'RGR']
    else:
        xx['r']=[r,0,r, 'R', 'RGR']

    if v:
        y -= 2*v
        if y <0:
            return False, ''
        xx['y']=[v+y, v, y, 'Y', 'YVY']
    else:
        xx['y']=[y,0,y,'Y', 'YVY']

    xx = xx.values()

    xx.sort(key=lambda item: item[0], reverse=True)
    if xx[0][0] > xx[1][0] + xx[2][0]:
        return False, ''
    if xx[1][0] == 0:
        return False, ''
    h1 = []
    h2 = []
    h3 = []

    for u in range(xx[0][0]):
        if xx[0][1]:
            h1.append(xx[0][4])
            xx[0][1] -=1
        else:
            h1.append(xx[0][3])
            xx[0][2] -=1
    for u in range(xx[1][0]):
        if xx[1][1]:
            h2.append(xx[1][4])
            xx[1][1] -= 1
        else:
            h2.append(xx[1][3])
            xx[1][2] -=1
    for u in range(xx[2][0]):
        if xx[2][1]:
            h3.append(xx[2][4])
            xx[2][1] -= 1
        else:
            h3.append(xx[2][3])
            xx[2][2] -= 1

    hh = []
    x1,x2,x3 = len(h1),len(h2),len(h3)
    for d in range(x2+x3-x1):
        hh.append(h1[d])
        hh.append(h2[d])
        hh.append(h3[d])
    for d in range(x1-x3):
        hh.append(h1[x2+x3-x1+d])
        hh.append(h2[x2+x3-x1+d])
    for d in range(x1-x2):
        hh.append(h1[x2+d])
        hh.append(h3[x2+x3-x1+d])
    return True, ''.join(hh)




for i in range(t):
    _ = fin.readline().split(' ')
    n,r,o,y,g,b,v = int(_[0]), int(_[1]),int(_[2]),int(_[3]),int(_[4]),int(_[5]),int(_[6])
    yes, ans = check(n,r,o,y,g,b,v, i)
    if yes:
        fout.write('Case #%d: %s\n' % (i+1, ans))
    else:
        fout.write('Case #%d: %s\n' % (i+1, 'IMPOSSIBLE'))
