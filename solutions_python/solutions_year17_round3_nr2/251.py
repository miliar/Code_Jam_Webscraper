x = open("B-small-attempt0.in")
z = open("B-small.out", "w")
n = int(x.readline()[:-1])
zs = ""

for i in range(n):
    a, b = x.readline()[:-1].split()
    a1 = []
    b1 = []
    a2 = []
    b2 = []
    for j in range(int(a)):
        c, d = x.readline()[:-1].split()
        a1.append(int(c))
        a2.append(int(d))
    for j in range(int(b)):
        c, d = x.readline()[:-1].split()
        b1.append(int(c))
        b2.append(int(d))
    a1.sort()
    a2.sort()
    b1.sort()
    b2.sort()
    al = 0
    bl = 0
    alu = []
    blu = []
    slu = []
    s = 0
    if len(a1) > 0 and len(b1) > 0:
        if a1[0] > b1[0]:
            c = a1
            a1 = b1
            b1 = c
            c = a2
            a2 = b2
            b2 = c
    elif len(b1) > 0:
        c = a1
        a1 = b1
        b1 = c
        c = a2
        a2 = b2
        b2 = c
    ast = a1[0]
    while len(a1) > 0:
        t = 0
        al += a2[0] - a1[0]
        a = a2[0]
        del a2[0]
        del a1[0]
        if len(b1) > 0 and len(a1) > 0:
            if a1[0] < b1[0]:
                alu.append(a1[0] - a)
            else:
                slu.append(b1[0] - a)
                s += 1
                while len(b1) > 0:
                    t = 1
                    bl += b2[0] - b1[0]
                    b = b2[0]
                    del b2[0]
                    del b1[0]
                    if len(b1) > 0 and len(a1) > 0:
                        if b1[0] < a1[0]:
                            blu.append(b1[0] - b)
                        else:
                            slu.append(a1[0] - b)
                            s += 1
                            break
                    elif len(b1) > 0:
                        blu.append(b1[0] - b)
        elif len(a1) > 0:
            alu.append(a1[0] - a)
    if t == 0:
        alu.append((1440 - a) + ast)
    else:
        slu.append((1440 - b) + ast)
    if s % 2 != 0:
        s += 1
    al += sum(alu)
    bl += sum(blu)
    while al > 720:
        amax = max(alu)
        al -= amax
        s += 2
        del alu[alu.index(amax)]
    while bl > 720:
        bmax = max(blu)
        bl -= bmax
        s += 2
        del blu[blu.index(bmax)]
    zs += "Case #" + str(i + 1) + ": " + str(s) + "\n"

z.write(zs[:-1])
z.close()
