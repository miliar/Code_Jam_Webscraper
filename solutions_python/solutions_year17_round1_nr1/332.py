def solve(ip,r,c):
    for i in range(r):
        # check row
        s = set(ip[i])
        if len(s) == 1 :
            continue
        nc = ""
        for j in range(c):
            if ip[i][j] == "?":
                if nc == "" :
                    k = j
                    while ip[i][k] == "?":
                        k += 1
                    nc = ip[i][k]
                ip[i][j] = nc
            else:
                nc = ip[i][j]

    nr = []
    for i in range(r):
        # check row
        s = set(ip[i])
        if (len(s) == 1) and ("?" in s) :
            if len(nr) == 0:
                k = i
                while ip[k][0] == "?":
                    k += 1

                nr = ip[k][:]

            ip[i] = nr[:]

        else:
            nr = ip[i][:]

    return ip


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        r,c = map(int,input().strip().split())
        ip = []
        for i in range(r):
            _temp = input().strip()
            _ip = [c for c in _temp]
            ip.append(_ip[:])

        res = solve(ip,r,c)
        print("Case #{0}:".format(ti + 1))
        for row in res:
            print("".join(row))
