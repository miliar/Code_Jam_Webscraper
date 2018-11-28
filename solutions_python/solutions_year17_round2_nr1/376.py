def solve(d, n, ks):
    ks = sorted(ks, key=lambda x: x[0], reverse=True)
    t = [0] * n
    i = 0
    for k, s in ks:
        t[i] = (d - k) / s
        i += 1
    x = max(t)
    return d/x

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        d, n = [int(x) for x in input().split(" ")]
        ks = [(0,0)] * n
        for j in range(n):
            ks[j] = [int(x) for x in input().split(" ")]
        res = solve(d, n, ks)
        print ("Case #%d: %f" % (i, res))


                
