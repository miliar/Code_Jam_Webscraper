def find_horse_meeting(ki, si, kj, sj, d):
    if (sj == si):
        return d

    x = (1.0 * (ki*sj - si*kj)) / (sj-si)
    return min(x, d)


def solve(d, horses):
    horses = sorted(horses, cmp=lambda x, y: x[1]-y[1])
    horses1 = []
    while horses:
        slowest_horse = horses.pop(0)
        horses1.append(slowest_horse)
        horses=filter(lambda x: x[0]<slowest_horse[0], horses)

    total_time = 0.0
    last_meet = d
    for i in xrange(len(horses1) - 1):
        h2 = horses1[i]
        h1 = horses1[i+1]
        meeting = find_horse_meeting(h1[0], h1[1], h2[0], h2[1], d)
        total_time += (1.0 * last_meet - meeting)/h2[1]
        last_meet = meeting

    first_horse = horses1[-1]
    total_time += (1.0* last_meet - first_horse[0])/first_horse[1]

    return (d * 1.0) / (total_time)

def solve_from_file(infile, outfile):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    t = int(fin.readline())
    res = []
    for case in xrange(t):
        d, n = map(int, fin.readline().split())

        h = []
        for line in xrange(n):
            h.append(map(int, fin.readline().split()))

        res.append("Case #{i}: {res}\n".format(
            i=case + 1,
            res=solve(d, h)
        ))

    fout.writelines(res)



if __name__ == "__main__":
    # print solve(2525, [(2400, 5)])
    # print solve(300, [(120, 60), (60, 90)])
    # print solve(100, [(80, 100), (70, 10)])
    solve_from_file("/Users/yoni/Dropbox/Google Code Jam/2017/1B/A.in", "/Users/yoni/Dropbox/Google Code Jam/2017/1B/A.out")
