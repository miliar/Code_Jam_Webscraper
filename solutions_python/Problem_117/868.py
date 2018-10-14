def column(m, i):
    return [row[i] for row in m]

f = open(r'B-large.in', 'r')
g = open(r'outputB.out', 'w')
t = int(f.readline())
for i in range(1, t+1):
    g.write("Case #"+str(i)+": ")
    k = f.readline().split()
    m = []
    possible = True
    for j in range(int(k[0])):
        m += [list(map(int,f.readline().split()))]
    for j in m:
        high = max(j)
        for l in range(int(k[1])):
            if (j[l] < high) and (j[l] != max(column(m, l))):
                    possible = False
                    break
            elif j[l] > high:
                possible = False
        if not possible:
            break
    if possible:
        g.write("YES\n")
    else:
        g.write("NO\n")
f.close()
g.close()
