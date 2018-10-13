from itertools import cycle, islice, chain


def solve(n, R, O, Y, G, B, V):

    if (R == O == G == B == 0) and (Y==V):
        return "YV"*Y
    if (R == Y == G == V == 0) and (O==B):
        return "OB"*O
    if (Y == O == V == B == 0) and (G==R):
        return "RG"*R

    if O > 2*B:
        return "IMPOSSIBLE"
    if G > 2*R:
        return "IMPOSSIBLE"
    if V > 2*Y:
        return "IMPOSSIBLE"
    return solve_for_one_color(n, R-2*G, Y-2*V, B-2*O, G, V, O)


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))

def solve_for_one_color(n, R, Y, B, RGR, YVY, BOB):
    if (2*(R+RGR)>n):
        return "IMPOSSIBLE"
    if (2*(Y+YVY) > n):
        return "IMPOSSIBLE"
    if (2*(B+BOB)>n):
        return "IMPOSSIBLE"

    s = ""
    r = ["R"] * R + ["RGR"] * RGR
    y = ["Y"] * Y + ["YVY"] * YVY
    b = ["B"] * B + ["BOB"] * BOB

    l = sorted([r, y, b], cmp=lambda x,y : len(y)-len(x))

    l0 = len(l[0])
    l1 = len(l[1])
    l2 = len(l[2])

    l0_0 = l[0][:l0-l1]
    l2_0 = l[2][:l0-l1]

    l0_1 = l[0][l0-l1:l2]
    l1_1 = l[1][:l2-(l0-l1)]
    l2_1 = l[2][l0-l1:]

    l0_2 = l[0][l2:]
    l1_2 = l[1][l2-l0+l1:]


    s += ''.join(list(roundrobin(l0_0, l2_0)))
    s += ''.join(list(roundrobin(l0_1, l1_1, l2_1)))
    s += ''.join(list(roundrobin(l0_2, l1_2)))

    interleave_first_and_third = len(l[0])

    return s

def solve_from_file(infile, outfile):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    t = int(fin.readline())
    res = []
    for case in xrange(t):
        nums = map(int, fin.readline().split())

        res.append("Case #{i}: {res}\n".format(
            i=case + 1,
            res=solve(*nums)
        ))

    fout.writelines(res)

if __name__ == "__main__":
    # print solve(6,2,0,2,0,2,0)
    # print solve(3,1,0,2,0,0,0)
    # print solve(6,2,0,1,1,2,0)
    # print solve(4,0,0,2,0,0,2)
    solve_from_file("/Users/yoni/Dropbox/Google Code Jam/2017/1B/B.in", "/Users/yoni/Dropbox/Google Code Jam/2017/1B/B.out")
