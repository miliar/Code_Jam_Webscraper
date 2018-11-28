def make_pair(a, b, ca, cb):
    if b == 0:
        return (a, '')
    if b + 1 > a:
        return None
    else:
        return (a - b - 1, (ca + cb) * b + ca)

def make_ryb(r, y, b, olr, oly, olb):

    cr,cy,cb = 'RYB'

    if y <= b:
        y,b = b,y
        oly, olb = olb, oly
        cy, cb = cb,cy

    if r <= y:
        y,r = r,y
        oly, olr = olr, oly
        cy, cr = cr,cy

    if y <= b:
        y,b = b,y
        oly, olb = olb, oly
        cy, cb = cb,cy

    if olr and oly and olb:
        if y + b < r:
            return None
        return (cr + cy + cb) * (b + y - r) + (cr + cy) * (r - b) + (cr + cb) * (r - y)


def stalls(n,r,o,y,g,b,v):
    rg = make_pair(r, g, 'R', 'G')
    yv = make_pair(y, v, 'Y', 'V')
    bo = make_pair(b, o, 'B', 'O')
    if rg is None or yv is None or bo is None:
        return "IMPOSSIBLE"
    ryb = make_ryb(rg[0], yv[0], bo[0], g is 0, v is 0, o is 0)
    if ryb is None:
        return "IMPOSSIBLE"

    if ryb[0] == 'r':
        return rg[1] + yv[1] + ryb + bo[1]
    if ryb[0] == 'y':
        return rg[1] + yv[1] + bo[1] + ryb
    return rg[1] + ryb + yv[1] + bo[1]

if __name__ == "__main__":
    with open("input") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(1, t + 1):
            n, r, o, y, g, b, v = map(int, fi.readline().split())
            #print("Case #{}: {}\n".format(i, stalls(n, r, o, y, g, b, v)))
            fo.write("Case #{}: {}\n".format(i, stalls(n, r, o, y, g, b, v)))
