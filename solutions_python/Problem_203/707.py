f = open("A-large.in")
l = []
for line in f:
    l.append(line.strip())
i = 1
case = 1
while i < len(l):
    r = int(l[i].split()[0])
    c = int(l[i].split()[1])
    m = []
    n_m = []
    for j in range(r):
        m.append([])
        n_m.append([])
        for k in range(c):
            m[j].append(l[i + 1 + j][k])
            n_m[j].append(l[i + 1 + j][k])
##    print(m)
    for j in range(r):
        for k in range(c):
            chara = ''
            if m[j][k] != '?':
                chara = m[j][k]
                for t in range(c):
                    if m[j][t] == '?':
                        m[j][t] = chara
                    else:
                        chara = m[j][t]
    for j in range(r):
        if m[j][0] == '?':
            if j == 0:
                k = 1
                while m[j + k][0] == '?':
                    k += 1
                for t in range(k):
                    m[j + t] = m[j + k][:]
            else:
                m[j] = m[j - 1][:]
    print("Case #{}:".format(case))
    for j in range(r):
        for k in range(c):
            print(m[j][k], end = '')
        print()
    case += 1
    i = i + r + 1
