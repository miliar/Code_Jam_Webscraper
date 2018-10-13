f = open("data.txt")
g = open("data1.txt", 'w')
j = int(f.readline())

for i in range(j):
    l = f.readline()
    n, k, b, t = (int(x) for x in l.split())
    l = f.readline()
    x = [int(x) for x in l.split()]
    l = f.readline()
    v = [int(x) for x in l.split()]
    feas = []
    for r in range(n):
        if (x[r] + (v[r] * t)) > b-1:
            feas.append(r)
    if len(feas) < k:
        stri = 'IMPOSSIBLE'
    else:
        feas = feas[-k:]
        c = 0
        for u in feas:
            for y in range(u+1, n):
                if y not in feas:
                    c += 1
        stri = str(c)
    string = 'Case #' + str(i+1) + ': ' + stri + '\n'
    g.write(string)
    print(string)
