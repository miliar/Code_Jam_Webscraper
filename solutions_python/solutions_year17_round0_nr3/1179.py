def level(n):
    k = 0
    a = 0
    while n-a > 0:
        a = a+ 2**k
        k += 1
    return k

def remain(n, k):
    a = 0
    for i in range(k-1):
        a = a + 2**(i)
    d = n-a
    return d

def setlr(n, k):
    a = []
    b = [n]
    for i in range(k-1):
        for j in b:
            if j%2 == 0:
                a.append(j/2)
                a.append((j/2)-1)
            else:
                a.append((j-1)/2)
                a.append((j-1)/2)
        b = a[:]
        a = []
        b.sort()
        b.reverse()
    return (b)

in_f = open("i.in", 'r')
ou_f = open("o.out", 'w')

T = int(in_f.readline())
for i in range(T):
    N, K = in_f.readline().strip().split(" ")
    n, k = int(N), int(K)
    l = level(k)
    r = remain(k, l)
    out_l = setlr(n, l)
    j = out_l[r-1]
    if j % 2 == 0:
        out1 = (j / 2)
        out2 = ((j / 2) - 1)
    else:
        out1 = ((j - 1) / 2)
        out2 = ((j - 1) / 2)

    j = "Case #" + str(i+1) +": " + str(int(out1))+ " " + str(int(out2)) + "\n"
    ou_f.write(j)
in_f.close()
ou_f.close()