z = open('D-large.in', 'r')
w = open('OUT.txt','w')
n = int(z.readline())

for q in range (n):
    k = int(z.readline())
    a = z.readline().strip().split()
    b = z.readline().strip().split()
    for i in range(len(a)):
        a[i] = float(a[i])
        b[i] = float(b[i])
    a.sort(reverse=True)
    b.sort(reverse=True)
    g1 = []
    g2 = []
    c1 = 0
    c2 = 0
    for i in range (len(a)):
        if b[c1] > a[i]:
            g1.append(1)
            c1 += 1
        if a[c2] > b[i]:
            g2.append(1)
            c2 += 1
    w.write ("Case #" + str(q+1) + ": " + str(len(g2)) + " " + str(k - len(g1)) + "\n")

z.close()
w.close()