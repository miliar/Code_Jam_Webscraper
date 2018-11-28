# coding=utf-8

import sys


def simu(hd, ad, hk, ak, b, d, b_cnt, d_cnt):
    hp = hd
    pre = False
    cnt = 0
    while True:
        cnt += 1
        if d_cnt > 0:
            if ak - d >= hp:
                if pre:
                    return 0
                pre = True
                hp = hd
            else:
                pre = False
                ak -= d
                d_cnt -= 1
        elif b_cnt > 0:
            if ak >= hp:
                if pre:
                    return 0
                pre = True
                hp = hd
            else:
                pre = False
                ad += b
                b_cnt -= 1
        else:
            if ad < hk and ak >= hp:
                if pre:
                    return 0
                pre = True
                hp = hd
            else:
                pre = False
                hk -= ad
        if hk <= 0:
            break
        hp -= ak
        if hp <= 0:
            return 0
    return cnt


def solve(hd, ad, hk, ak, b, d):
    if ad >= hk:
        return 1
    if ak - d >= hd:
        return 0
    b_cnt = 0
    if b > 0:
        b_cnt = min(100, hk)
    d_cnt = 0
    if d > 0:
        d_cnt = ak
    res = 0
    i = 0
    while i <= b_cnt:
        j = 0
        while j <= d_cnt:
            r = simu(hd, ad, hk, ak, b, d, i, j)
            if res == 0 or 0 < r < res:
                res = r
            j += 1
        i += 1
    return res


def main(argv=None):
    if argv is None:
        argv = sys.argv
    infile = argv[1]
    outfile = argv[2]
    pin = open(infile, "r")
    pout = open(outfile, "w")
    n = int(pin.readline().strip())
    for i in range(n):
        hd, ad, hk, ak, b, d = pin.readline().strip().split(" ")
        hd = int(hd)
        ad = int(ad)
        hk = int(hk)
        ak = int(ak)
        b = int(b)
        d = int(d)
        print("#", str(i + 1))
        res = solve(hd, ad, hk, ak, b, d)
        pout.write("Case #" + str(i + 1) + ": " + ("IMPOSSIBLE" if res == 0 else str(res)) + "\n")
    pin.close()
    pout.close()


if __name__ == "__main__":
    main()
