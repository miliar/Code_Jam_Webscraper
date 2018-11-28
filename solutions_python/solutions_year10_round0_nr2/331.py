import sys, string, fractions

def solve():
    cases = 1
    t = int(input())
    while (t > 0):
        st = input().split(" ")
        n = -1
        l = []
        for s in st:
            if (n == -1):
                n = int(s)
            else:
                l.append(int(s))
        l.sort()
        x = 1
        g = l[1] - l[0]
        while x < len(l):
            g = fractions.gcd(g, l[x] - l[x - 1])
            x += 1
        r = g - (l[0] % g)
        if g == r:
            r = 0
        print("Case #" + str(cases) + ": " + str(r))
        cases += 1
        t -= 1
    

solve()
