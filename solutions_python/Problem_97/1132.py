#! /usr/bin/python
# Google Code Jam 2012 - Qualification
# Problem C - Recycled Numbers

def solve(a, b):
    res = 0
    resl = []
    for i in range(1, len(str(a))):
        for x in range(a, b+1):
            sx = str(x)
            if sx[i]!='0':
                sx = sx[i:]+sx[:i]
                isx = int(sx)
                if x!=isx and isx>=x and isx<=b:
                    if (x, isx) not in resl:
                        resl.append((x, isx))
                        res += 1
    return res

if __name__ == "__main__":
    t = input()
    for ti in range(1, t+1):
        inp = raw_input().split(" ")
        a = int(inp[0])
        b = int(inp[1])
        print "Case #%d: %d" % (ti, solve(a, b))


