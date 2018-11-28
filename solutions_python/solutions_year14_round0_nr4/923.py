#in_f = open('D-small-attempt0.in.txt', 'r')
in_f = open('D-large.in.txt', 'r')
out_f = open('output', 'w')

t = int(in_f.readline())
for t in range(1, t+1):
    print 'processing %d case' % t
    n = int(in_f.readline())
    y = n
    z = 0
    a = []
    b = []
    aa = in_f.readline().split(' ')
    bb = in_f.readline().split(' ')
    for ai in aa:
        a.append(float(ai))
    for bi in bb:
        b.append(float(bi))
    a.sort()
    b.sort()
    i = 0
    j = 0
    while i < n and j < n:
        while j < n and b[j] < a[i]:
            j += 1
        if j == n:
            break
        i += 1
        j += 1
    z = n - i

    i = 0
    j = 0
    while i < n and j < n:
        while i < n and a[i] < b[j]:
            i += 1
        if i == n:
            break
        i += 1
        j += 1
    y = j
    out_f.write('Case #%d: %d %d\n' % (t, y, z))
    print a
    print b
    print ('Case #%d: %d %d' % (t, y, z))
in_f.close()
out_f.close()



