def count(A, B):
    res = 0
    for n in range(A, B):
        s = str(n)
        d = {}
        for j in range(1, len(s)):
            m = s[j:] + s[:j]
            if m[0] == '0':
                continue
            m = int(m)
            if m <= B and n < m and m not in d:
                d[m] = d.get(m, 0) + 1
                res += 1
    return res

g = open("output.txt", 'w')
with open("C-large.in") as f:
    N = int(f.readline())
    for i in range(N):
        s = f.readline()
        k = s.split()
        A = int(k[0])
        B = int(k[1])

        res = count(A, B)
        out = "Case #%d: %d\n" % (i+1, res)
        print out
        g.write(out)

g.close()

