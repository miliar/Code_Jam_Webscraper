def gcd(l1, l2):
    if (l2 == 0):
        return l1
    return gcd(l2, l1 % l2)

inf = open("input.txt")
outf = open("output.txt", "w")
s = inf.readline()
c = int(s.split(" ")[0])
for i in range(c):
    ns = []
    s = inf.readline()
    li = s.split(" ")
    n = long(li[0])
    for j in range(n):
        ns.append(long(li[j + 1]))
    ns.sort()
    ds = []
    for k in range(len(ns) - 1):
        ds.append(ns[k + 1] - ns[k])
    g = ds[0];
    for k in ds:
        g = gcd(g, k)
    if ((ns[0] % g) == 0):
        outf.write("Case #" + str(i + 1) + ": " + "0\n")
    else:
        outf.write ( "Case #" + str(i + 1) + ": " + str(g - (ns[0] % g)) + "\n" )
inf.close()
outf.close()
