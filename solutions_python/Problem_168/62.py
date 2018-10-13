__author__ = 'PrimuS'


f = open("d:\\dev\\acm\\codeJam 2015\\A-large.in", "r")
of = open("d:\\dev\\acm\\codeJam 2015\\Alres.txt", "w")

T = int(f.readline())

for t in range(1, T + 1):
    r, c = (int (x) for x in f.readline().split())
    s = [0] * r
    for i in range(r):
        s[i] = f.readline().strip()

    ok = True
    res = 0

    for i in range(r):
        for j in range(c):

            if s[i][j] != '.':
                rr = False
                for k in range(j + 1, c):
                    if s[i][k] != '.':
                        rr = True
                        break
                ll = False
                for k in range(0, j):
                    if s[i][k] != '.':
                        ll = True
                        break

                uu  = False
                for k in range(0, i):
                    if s[k][j] != '.':
                        uu = True
                        break

                dd  = False
                for k in range(i+1, r):
                    if s[k][j] != '.':
                        dd = True
                        break

                if not (ll or rr or dd or uu):
                    ok = False
                else:
                    if (s[i][j] == '<' and ll) or (s[i][j] == '>' and rr) or (s[i][j] == '^' and uu) or (s[i][j] == 'v' and dd):
                        pass
                    else:
                        res += 1


    if (ok):
        print("Case #{:d}: {:d}".format(t, res), file=of)
    else:
        print("Case #{:d}: IMPOSSIBLE".format(t), file=of)

of.close()
