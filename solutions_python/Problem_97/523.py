def rearrange(a,b):
    x = [a]
    k = 0
    for i in range(1,len(a)):
        if (a[-i] <= b[0]) and (a[-i] >=a[0]):
            u = a[-i:] + a[:-i]
            if (u<=b) and (u>a) and (u not in x):
                k = k + 1
                x.append(u)
    return(k)

fh = open("a.in",'r')
fhw = open("b.txt",'w')
f = fh.readlines()
x = int(f[0].strip())
y1 = f[1:]
i = 0
d = {}
l = 1
for t in y1:
    k = 0
    y = t.strip().split()
    A = int(y[0])
    B = int(y[1])
    for j in range(A,(B + 1)):
        j1 = str(j)
        z = rearrange(j1,y[1])
        k = k + z
    d[l] = "Case #" + str(l) +": " + str(k)
    l = l + 1
for p in range(1,x):
    fhw.write(d[p] + "\n")
fhw.write(d[x])
fh.close()
fhw.close()
