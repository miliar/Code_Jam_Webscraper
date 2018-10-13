import os

def gcd(a, b):
    while(b != 0):
        r = b
        b = a % b
        a = r
    return a

#fin = open("test.txt")
fin = open("B-large.in")
fout = open("out.txt", "w")
t = int(fin.readline())
for i in range(t):
    param = fin.readline().split()
    n = int(param[0])
    ll = []
    ld = []
    for j in range(n):
        ll.append(int(param[j + 1]))
    for j in range(n):
        for k in range(n)[j+1:]:
            ld.append(abs(ll[j] - ll[k]))
    #print ld
    for l in ld[1:]:
        #print gcd(ld[0], l)
        ld[0] = gcd(ld[0], l)
    #print ll, ld
    #print ll[0] % ld[0]
    if ld[0] == 1 or ll[0] % ld[0] == 0:
        res = 0
    else:
        res = ld[0] - ll[0] % ld[0]
        
    fout.write("Case #%d: %s\n" % (i + 1, str(res)))

