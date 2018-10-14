#! coding: utf-8

if __name__ == '__main__':

    #python2:
    T = int(raw_input())
    for i in xrange(T):
        N, K = [int(s) for s in raw_input().split(" ")]
        U = float(raw_input())
        P = [float(s) for s in raw_input().split(" ")]
        P.sort()
        PS = [P[0]]
        for j in xrange(1, N):
            PS.append(PS[j - 1] + P[j])
        res = 1
        for j in xrange(N - 1, 0, -1):
            curr = j * P[j] - PS[j - 1]
            if U >= curr:
                res *= (P[j] + float(U - curr) / float(j + 1)) ** (j + 1)
                break
            res *= P[j]
        else:
            res *= (P[0] + U)
        print("Case #{0}: {1}".format(i + 1, res))
