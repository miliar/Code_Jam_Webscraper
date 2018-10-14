x = open("C-small-1-attempt0.in")
z = open("C-small-1-attempt0.out", "w")
n = int(x.readline()[:-1])
zs = ""

for i in range(n):
    m, k = x.readline()[:-1].split()
    m = int(m)
    k = int(k)
    l = [m]
    for j in range(k - 1):
        y = max(l)
        l.remove(y)
        if y % 2 != 0:
            l.append((y - 1) // 2)
            l.append((y - 1) // 2)
        else:
            l.append((y - 2) // 2)
            l.append(y // 2)
    y = max(l)
    if y % 2 != 0:
        a = (y - 1) // 2
        b = (y - 1) // 2
    else:
        a = (y - 2) // 2
        b = y // 2
    zs += "Case #" + str(i + 1) + ": " + str(b) + " " + str(a) + "\n"
    
z.write(zs[:-1])
z.close()
