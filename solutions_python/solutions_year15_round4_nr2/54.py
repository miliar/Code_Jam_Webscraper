for T in range(1, input()+1):
    inp = raw_input().split()
    N = int(inp[0])
    V = float(inp[1])
    X = float(inp[2])

    data = []

    for i in range(N):
        data.append(map(float, raw_input().split()))

    Rhot, Xhot, hot = 0, 0, False
    Rcold, Xcold, cold = 0, 0, False
    Rexact = 0

    for i in range(N):
        if data[i][1] < X:
            if cold is False:
                Rcold, Xcold = data[i][0], data[i][1]
                cold = True
            else:
                Rcold, Xcold = (Rcold + data[i][0]), ((Rcold*Xcold + data[i][0]*data[i][1]) / (Rcold + data[i][0]))
        elif data[i][1] > X:
            if hot is False:
                Rhot, Xhot = data[i][0], data[i][1]
                hot = True
            else:
                Rhot, Xhot = (Rhot + data[i][0]), ((Rhot*Xhot + data[i][0]*data[i][1]) / (Rhot + data[i][0]))
        else:
            Rexact += data[i][0]

    if not cold or not hot:
        if Rexact == 0:
            ans = 'IMPOSSIBLE'
        else:
            ans = V / Rexact
    else:
        Rcold, Xcold = (Rcold + Rexact), ((Rcold*Xcold + Rexact*X) / (Rcold + Rexact))

        A = Rhot * Xhot
        B = Rcold * Xcold
        C = V * X
        D = Rhot
        E = Rcold
        F = V

        ans_cold = (C / A - F / D) / (B / A - E / D)
        ans_hot = (V - (E * ans_cold)) / D

        ans = max(ans_cold, ans_hot)

    print "Case #{}: {}".format(T, "%.9f" % ans if type(ans) is float else ans)
