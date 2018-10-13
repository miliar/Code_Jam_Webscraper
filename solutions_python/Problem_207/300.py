nko = 0
red = 1
oran = 2
yel = 3
green = 4
blue = 5
viol = 6

T = int(input())
for t in range(1, T+1):
    inp = [int(x) for x in input().split()]
    n = inp[nko]
    cols2 = [(inp[red], "R"), (inp[blue], "B"), (inp[yel], "Y")]
    cols2.sort()
    cols = []
    i = 0
    for p,col in cols2:
        cols.append((p, i, col))
        i += 1
    odp = ""
    last = ""
    nedasa = False
    for i in range(n):
        cols.sort()
        #print(cols, odp)
        kto = 2
        if cols[kto][2] == last:
            kto = 1
        if cols[kto][0] == 0:
            nedasa = True
            break
        odp += cols[kto][2]
        cols[kto] = (cols[kto][0] - 1, cols[kto][1], cols[kto][2])
        last = cols[kto][2]
    print("Case #%d: " % t, end="")
    if not nedasa and odp[n-1] == odp[0]:
        nedasa = True
    if nedasa:
        print("IMPOSSIBLE")
    else:
        print(odp)
