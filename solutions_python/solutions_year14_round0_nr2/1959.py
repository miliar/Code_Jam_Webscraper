def cookie(c, f, x):
    t, d, r = 0, 0, 2
    while d < x:
        ttx = (x - d) / r
        ttf = (c - d) / r
        if ttx < ttf:
            return t + ttx
        t += ttf
        d += ttf * r
        if (x - d) / r < x / (r + f):
            return t + (x - d) / r
        d = 0
        r += f

def main():
    n = int(input())
    for i in range(n):
        c, f, x = map(float, input().split())
        ans = cookie(c, f, x)
        print("Case #{}: {}".format(i+1, ans))

main()
