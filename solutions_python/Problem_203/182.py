fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    r, c = [int(s) for s in fin.readline().strip().split(" ")]
    cake = []
    for j in range(r):
        cake.append(list(fin.readline().strip()))
    for j in range(r):
        for k in range(c):
            if cake[j][k] == '?':
                u = k
                while u < c and cake[j][u] == '?':
                    u = u + 1
                if u < c:
                    cake[j][k] = cake[j][u]
                elif k>0:
                    cake[j][k] = cake[j][k - 1]
    for j in range(r):
        for k in range(c):
            if cake[j][k] == '?':
                u = j
                while u < r and cake[u][k] == '?':
                    u = u + 1
                if u < r:
                    cake[j][k] = cake[u][k]
                else:
                    cake[j][k] = cake[j - 1][k]

    # print>>fout, "Case #{}: {} {}".format(i, n + m, n * m)
    print>> fout, "Case #{}:".format(i)
    for j in range(r):
        print>> fout, ''.join(cake[j])

fin.close()
fout.close()
