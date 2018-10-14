inf = open('input.txt', 'r')
c = int(inf.readline())
for i in range(c):
    line = inf.readline().split()
    t = []
    for j in range(1, len(line)):
        t.append(int(line[j]))
    t.sort()
    gcd = t[1] - t[0];
    for j in range(1, len(t)):
        a = gcd;
        b = t[j] - t[j - 1]
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a % b
        gcd = a
    y = gcd - t[0] % gcd;
    if y == gcd:
        y = 0
    print 'Case #%(i)d: %(y)d' % {'i': i + 1, 'y': y}
