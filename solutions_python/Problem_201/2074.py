
OUTP_FORMAT = "Case #{}: {} {}"

T = int(raw_input())

"""
DOES THE WORK
"""
def find_stall(N, I):

    res = []
    mn = [[min(i, N - i - 1), max(i, N - i - 1), 0] for i in xrange(N)]
    # print mn
    for x in xrange(I):
        m = max(mn, key=lambda x: min(x[0], x[1]))
        m2 = [a for a in mn if min(a[0], a[1]) == min(m[0],m[1])]
        m3 = max(m2, key=lambda x: max(x[0], x[1]))
        m4 = [a for a in m2 if max(a[0], a[1]) == max(m3[0],m3[1])]
        # print m3, m4
        a = m3
        i = mn.index(a)
        mn[i][2] = 1
        res = mn[i]
        ones = [a for a in mn if a[2] == 1]
        cn = 0
        for y in xrange(n):
            if mn[y][2] == 1:
                mn[y] = [-1, -1, 1]
                ones.pop(0)
                cn = 0
            else:
                if len(ones) > 0:
                    mn[y] = [cn, mn.index(ones[0], y) - y - 1, 0]
                else:
                    mn[y] = [cn, n - y - 1, 0]

                cn += 1
    return max(res[1], res[0]), min(res[1],res[0])


for i in xrange(T):
    n, m = [int(x) for x in raw_input().strip().split()]
    y, z = find_stall(n, m)
    print OUTP_FORMAT.format(i+1, y, z)
