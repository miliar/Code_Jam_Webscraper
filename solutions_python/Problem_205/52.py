import math

fin = open('C-small-attempt4.in', 'r')
fout = open('C-small-attempt4.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    hd, ad, hk, ak, b, d = [int(s) for s in fin.readline().strip().split(" ")]
    if ad >= hk:
        print>> fout, "Case #{}: {}".format(i, 1)
        continue
    if max(ad + b, ad + ad) >= hk and hd > ak:
        print>> fout, "Case #{}: {}".format(i, 2)
        continue
    if hd <= ak - d + ak - 2 * d:
        print>> fout, "Case #{}: {}".format(i, 'IMPOSSIBLE')
        continue

    r_attack = 10000000
    for j in range(0, 100):
        temp_r = math.ceil(hk * 1.0 / (b * j + ad)) + j
        r_attack = min(temp_r, r_attack)
    r_attack = int(r_attack)

    r_cure = 10000000
    for x in range(0, 101):
        t_hd = hd
        t_ak = ak
        t_cure = x
        if x > 0:
            for j in range(x):
                if t_hd <= t_ak - d:
                    t_cure += 1
                    t_hd = hd - t_ak
                t_ak -= d
                if t_ak < 0:
                    t_ak = 0
                t_hd -= t_ak
        if r_attack > 1:
            if hd <= t_ak + t_ak:
                continue
            for j in range(r_attack - 1):
                if t_hd <= t_ak:
                    t_cure += 1
                    t_hd = hd - t_ak
                t_hd -= t_ak
        if t_cure < r_cure:
            r_cure = t_cure
    r_cure = int(r_cure)
    print>>fout, "Case #{}: {}".format(i, r_attack + r_cure)
fin.close()
fout.close()
