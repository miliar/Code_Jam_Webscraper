fi = open('B-small-attempt1.in', 'r')
fo = open('outputB-small.txt', 'w')

T = int(fi.readline())

for t in range(T):

    linetok = fi.readline().split()
    n = int(linetok[0])
    N = n
    c = [0] * 6
    ch = [''] * 6
    c[0] = int(linetok[1])
    c[1] = int(linetok[2])
    c[2] = int(linetok[3])
    c[3] = int(linetok[4])
    c[4] = int(linetok[5])
    c[5] = int(linetok[6])
    ch[0] = 'R'
    ch[1] = 'O'
    ch[2] = 'Y'
    ch[3] = 'G'
    ch[4] = 'B'
    ch[5] = 'V'
    st = ''

    i = c.index(min([n for n in c if n > 0]))
    iinit = i
    r = 0
    ln = -2
    while n > 0 and r < N * 6:
        if (c[i] > 0 and (ln < -1 or (abs(ln - i) > 1.5))):
            if (t == 1):
                print(c[i], ln, i, abs(ln - i))
            c[i] -= 1
            n -= 1
            st += ch[i]
            ln = i
            r = 0

        if (r == 0):
            m1 = c[(i+2) % 6]
            m2 = c[(i+3) % 6]
            m3 = c[(i+4) % 6]
            if m2 > 0:
                i = (i+3) % 6
            elif max(m1, m3) == m1:
                i = (i+2) % 6
            else:
                i = (i+4) % 6
        else:
            i = (i+1) % 6
        r += 1
        
    isvalid = (r != N * 6) and (abs(iinit - ln) > 1.5)

    if isvalid:
        fo.write('Case #{0}: {1}\n'.format(t+1, st))
    else:
        fo.write('Case #{0}: IMPOSSIBLE\n'.format(t+1))
    
fi.close()
fo.close()
