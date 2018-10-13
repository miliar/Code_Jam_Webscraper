def solve(a, b):
    global rez, alpha
    t = [list[a-1][b], list[a][b-1], list[a][b+1], list[a+1][b]]
    m = min(t)
    goto = t.index(m)
    # ce ni se vrednosti na sinku vzamemo nasledno vrednost iz seznama
    # in popravimo od spodaj navzgor
    if m >= list[a][b]: #found sink
        if not rez[a-1][b-1]:
            rez[a-1][b-1] = alpha.pop(0)
        return rez[a-1][b-1]
    elif goto == 0:
        x = a-1
        y = b
    elif goto == 1:
        x = a
        y = b-1
    elif goto == 2:
        x = a
        y = b+1
    elif goto == 3:
        x = a+1
        y = b
    if rez[x-1][y-1]:
        rez[a-1][b-1] = rez[x-1][y-1]
    else:
        rez[a-1][b-1] = solve(x, y)
    return rez[a-1][b-1]


f = open("B-large.in")
a = f.readlines()
T = int(a.pop(0).strip())

for i in range(T):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    H,W = [int(j) for j in a.pop(0).strip().split(" ")]
    list = [11111]*(H+2)
    rez = [0]*H
    for k in range(1,H+1):
        list[k] = [11111]+[int(j) for j in a.pop(0).strip().split(" ")]+[11111]
        rez[k-1] = [False]*W
    list[0] = [11111]*(W+2)
    list[-1] = [11111]*(W+2)
    for j in range(1,H+1):
        for k in range(1,W+1):
            if not rez[j-1][k-1]:
                solve(j,k)
    print "Case #" + str(i+1)+":"
    for x in rez:
        for y in x:
            print y,
        print ""