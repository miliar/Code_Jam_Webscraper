__author__ = 'PrimuS'

f = open("d:\\dev\\acm\\codeJam 2015\\B-large.in", "r")
of = open("d:\\dev\\acm\\codeJam 2015\\B_res_big.txt", "w")

T = int(f.readline())
# T = 100
for t in range(1, T + 1):
    d = int(f.readline())
    # d = 1000
    p = [int(x) for x in f.readline().split()]
    # p = [1000] * 1000
    up = max(p)
    best_res = up
    for i in range(1, up + 1):
        cur = 0
        for x in p:
            fr = (x + (i-1)) // i
            cur += fr - 1
        best_res = min(best_res, cur + i)
    print(t)
    print("Case #{:d}: {:d}".format(t, best_res), file=of)

of.close()