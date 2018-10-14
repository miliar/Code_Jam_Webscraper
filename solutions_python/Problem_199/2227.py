#coding: utf-8 -*-

def solve(S, K):
    if S.find("-") == -1:
        return 0

    N = 0
    SL = len(S)

    while 1:
        f = S.find("-")
        if f == -1:
            return N #virou tudo

        if SL - f < K:
            return "IMPOSSIBLE"

        r = S[f:f+K]
        r = r.replace("-", "0").replace("+", '-').replace("0", "+")

        S = S[:f] + r + S[f+K:]
        N = N+ 1



T = int(raw_input())

case = 1

while case <= T:
    line = raw_input()
    S, K = line.split(" ")
    K = int(K)
    print "Case #%d: %s" % (case, str(solve(S, K)))
    case = case + 1

