x = open("A-large.in")
z = open("A-large.out", "w")
n = int(x.readline()[:-1])
zs = ""

for i in range(n):
    l = []
    c = 0
    s, k = x.readline()[:-1].split()
    k = int(k)
    for j in s:
        l.append(j)
    for j in range(len(l) - k + 1):
        if l[j] == "-":
            c += 1
            for m in range(k):
                if l[j + m] == "-":
                    l[j + m] = "+"
                else:
                    l[j + m] = "-"
    if "-" in l:
        zs += "Case #" + str(i + 1) + ": IMPOSSIBLE" + "\n"
    else:
        zs += "Case #" + str(i + 1) + ": " + str(c) + "\n"

z.write(zs[:-1])
z.close()
