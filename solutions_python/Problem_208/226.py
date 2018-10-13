# Problem C

def solve2(prd, phsp, cp, n , h , dist):
    if cp == n-1:
        return 0

    hd, hsp = h[cp]
    d = dist[cp]
    t = d/hsp

    if (d > prd) or ((hsp > phsp) and (hd >= prd)):
        return t + solve2(hd-d, hsp, cp+1, n, h, dist)
    else:
        t0 = d/phsp
        return min(t + solve2(hd-d, hsp, cp+1, n, h, dist) ,
        t0 + solve2(prd - d, phsp, cp+1, n, h, dist)  )


def solve(n,h,dist):
    res = 0

    cp = 0
    hd, hsp = h[0]
    d = dist[0]

    t = d/hsp

    return t + solve2(hd-d, hsp, 1, n , h , dist)


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        n,q = map(int,input().split(" "))
        h = []
        dist = []
        for _ in range(n):
            h.append(list(map(int,input().split(" "))))

        for ni in range(n):
            dm = list(map(int,input().split(" ")))
            if ni < (n-1):
                dist.append(dm[ni+1])
            else:
                dist.append(0)

        qr = []
        for qi in range(q):
            qr.append(list(map(int,input().split(" "))))

        print("Case #{0}: {1}".format(ti + 1, solve(n,h,dist)))
