#! /usr/bin/python
# Google Code Jam 2012 - Qualification
# Problem B - Dancing With the Googlers

def solve(n, s, p, l):
    res = 0
    for li in l:
        if p == 0:
            res += 1
        elif li > 0:
            v = li / 3
            r = li % 3
            if r == 0:
                if v >= p:
                    res += 1
                elif s>0 and v+1>=p:
                    res += 1
                    s -= 1
            elif r == 1:
                if v+1 >= p:
                    res += 1
            elif r == 2:
                if v+1 >= p:
                    res += 1
                elif s>0 and v+2>=p:
                    res += 1
                    s -= 1
    return res

if __name__ == "__main__":
    t = input()
    for ti in range(1, t+1):
        inp = raw_input().split(" ")
        n = int(inp[0])
        s = int(inp[1])
        p = int(inp[2])
        l = []
        for ni in range(3, n+3):
            l.append(int(inp[ni]))
        print "Case #%d: %d" % (ti, solve(n, s, p, l))


