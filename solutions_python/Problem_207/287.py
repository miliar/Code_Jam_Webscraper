fin = open('B-small-attempt0.in')
fout = open('output.txt', 'w')
T = int(fin.readline())
for tt in range(T):
    N, R, O, Y, G, B, V = map(int, fin.readline().split(' '))
    S = R + B + Y
    res = "IMPOSSIBLE"
    if R >= Y and R >= B:
        if Y + B >= R:
            res = [""] * S
            for i in range(R):
                res[2 * i] = "R"
            t = (S + 1) / 2 - R
            if Y < B:
                for i in range(t):
                    res[2 * R + i * 2] = "Y"
                Y -= t
                for i in range(Y):
                    res[2 * i + 1] = "Y"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "B"
            else:
                for i in range(t):
                    res[2 * R + i * 2] = "B"
                B -= t
                for i in range(B):
                    res[2 * i + 1] = "B"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "Y"
    elif B >= Y and B >= R:
        if Y + R >= B:
            res = [""] * S
            for i in range(B):
                res[2 * i] = "B"
            t = (S + 1) / 2 - B
            if Y < R:
                for i in range(t):
                    res[2 * B + i * 2] = "Y"
                Y -= t
                for i in range(Y):
                    res[2 * i + 1] = "Y"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "R"
            else:
                for i in range(t):
                    res[2 * B + i * 2] = "R"
                R -= t
                for i in range(R):
                    res[2 * i + 1] = "R"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "Y"
    else:
        if B + R >= Y:
            res = [""] * S
            for i in range(Y):
                res[2 * i] = "Y"
            t = (S + 1) / 2 - Y
            if B < R:
                for i in range(t):
                    res[2 * Y + i * 2] = "B"
                B -= t
                for i in range(B):
                    res[2 * i + 1] = "B"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "R"
            else:
                for i in range(t):
                    res[2 * Y + i * 2] = "R"
                R -= t
                for i in range(R):
                    res[2 * i + 1] = "R"
                for i in range(S):
                    if res[i] == "":
                        res[i] = "B"
    # print ''.join(res)
    fout.write("Case #%s: %s\n" % (tt + 1, ''.join(res)))
fin.close()
fout.close()