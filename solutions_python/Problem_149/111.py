fin = open('B-small-attempt1.in', 'r')
fout = open('out3.txt', 'w')
t = int(fin.readline())
for cc in range(1, t + 1):
    n = int(fin.readline())
    a = [int(x) for x in fin.readline().split()]
    sa = a[:]
    maxa = max(sa)
    maxindex = sa.index(maxa)
    sa.pop(maxindex)
    sa.sort()
    result = 1000
    for chosen in range(0, 2 ** (n - 1)):
        b = []
        for i in range(0, n - 1):
            if (chosen >> i) & 1 == 1:
                b.append(sa[i])
        b.append(maxa)
        for i in range(n - 2, -1, -1):
            if (chosen >> i) & 1 == 0:
                b.append(sa[i])
        c = [x for x in range(0, n)]
        d = [0] * n
        for i in range(0, n):
            d[i] = c[b.index(a[i])]
        invpair = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if d[i] > d[j]:
                    invpair += 1
        if invpair < result:
            result = invpair
        if cc == 9 and invpair == 6:
            print(b)
    fout.write('Case #%d: %d\n' % (cc, result))
fin.close()
fout.close()
            
