def solve( N, K ):
    room = [0]*N
    if K == 1:
        S = int((N-1)/2)
        ls = S
        rs = N-S-1
        room[S] = 1
        return [max(ls, rs), min(ls, rs)]

    S = -1
    D = -1
    als = -1
    ars = -1
    k=0

    for k in range(K):
        if room.count(1) == 0:
            room[ int((N-1)/2) ] = 1
            continue
        else:
            S = -1
            D = -1
            als = -1
            ars = -1

            i = 0
            counter = room.count(1)
            prev = -1
            while i < N:
                if counter == 0:
                    break

                if room[i] == 1:
                    S_cand = int( (i + prev)/2 )
                    ls = S_cand - prev
                    prev = i
                    rs = i - S_cand
                    d = min(ls, rs)
                    if d > D:
                        S = S_cand
                        D = d
                        als = ls
                        ars = rs
                    elif d == D:
                        if max(ls, rs) > max(als, ars):
                            S = S_cand
                            D = d
                            als = ls
                            ars = rs
                    counter = counter - 1
                i = i+1

            S_cand = int( (N+prev)/2 )
            ls = S_cand - prev
            rs = N - S_cand
            d = min(ls, rs)
            if d > D:
                S = S_cand
                D = d
                als = ls
                ars = rs
            elif d == D:
                if max(ls, rs) > max(als, ars):
                    S = S_cand
                    D = d
                    als = ls
                    ars = rs

            room[S] = 1

    return [ max(als, ars)-1, min(als, ars)-1 ]

t = int(input())

for i in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    maximum, minimum = solve(n, k)
    print( "Case #{}: {} {}".format(i, maximum, minimum) )
