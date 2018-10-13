z = []
with open('t.txt') as t:
    for l in t:
        z.append(l.split())


for i in range(1, len(z)):
    m = z[i][0]
    n = z[i][1]

    f = 0
    s = 0

    for j in range(len(n)):
        if s >= j:
            s += int(n[j])
        else:
            p = j - s
            f += p
            s += p + int(n[j])





    print("Case #" + str(i) + ": " + str(f))

