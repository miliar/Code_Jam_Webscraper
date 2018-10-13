# lizesheng
#


def solve(cake, r, c):
    used = set()
    for i in range(r):
        for j in range(c):
            l = cake[i][j]
            if l != '?' and l not in used:
                used.add(l)
                expand(cake, i, j)
    for row in cake:
        print(''.join(row))


def expand(cake, i, j):
    r, c = len(cake), len(cake[0])
    l = cake[i][j]
    jl = jr = j
    iu = id = i
    llen = rlen = ulen = dlen = 0
    while jl != 0:
        jl -= 1
        if cake[i][jl] == '?':
            cake[i][jl] = l
            llen += 1
            continue
        else:
            break
    while iu != 0:
        iu -= 1
        if cake[iu][j] == '?':
            if all(cake[iu][jj]=='?' for jj in range(j-llen, j+1)):
                for jj in range(j-llen, j+1):
                    cake[iu][jj] = l
                ulen += 1
            else:
                break
        else:
            break
    while jr != c-1:
        jr += 1
        if cake[i][jr] == '?':
            if all(cake[ii][jr]=='?' for ii in range(i-ulen, i+1)):
                for ii in range(i-ulen, i+1):
                    cake[ii][jr] = l
                rlen += 1
            else:
                break
        else:
            break
    while id != r-1:
        id += 1
        if cake[id][j] == '?':
            if all(cake[id][jj]=='?' for jj in range(j-llen, j+rlen+1)):
                for jj in range(j-llen, j+rlen+1):
                    cake[id][jj] = l
                    # print(i, j, l, id, jj, j-llen, j+rlen+1)
            else:
                break
        else:
            break


t = int(input())
for icase in range(1, t + 1):
    a, b = input().split(" ")
    a, b = int(a), int(b)
    cake = []
    for i in range(a):
        cake.append([s for s in input()])
    # print(cake)
    print("Case #{}:".format(icase))
    solve(cake, a, b)
