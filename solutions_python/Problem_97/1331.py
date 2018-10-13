#!/usr/bin/python

fin = open("recycled.in")
fout = open("recycled.out","w")
T = int(fin.readline())
for i in range(T):
    A,B = map(int, fin.readline().strip().split(" "))
    n = len(str(A))
    found = 0
    for j in range(A,B+1):
        s = str(j)
        pairs = []
        for p in range(n-1):
            k = int(s[p+1:]+s[:p+1])
            if A<=k and k<=B and k < j and k not in pairs:
                found += 1
                pairs.append(k)
    fout.write("Case #"+str(i+1)+": "+str(found)+"\n")
fin.close()
fout.close()
