import sys
input = open(sys.argv[1])


def good(s, k, i, j, ii, jj):
    g = False
    for a in range(i, ii + 1):
        for b in range(j, jj + 1):
            if s[a][b] not in [k, '?']:
                return False
            if s[a][b] == k:
                g = True
    return g


def find_n_fill(s, k, r, c):
    mi, mj, mii, mjj, m = 0, 0, 0, 0, 0
    for i in range(r):
        for j in range(c):
            for ii in range(i, r):
                for jj in range(j, c):
                    if good(s, k, i, j, ii, jj) and m < (ii - i + 1) * (jj - j + 1):
                        # print (k, i, j, ii, jj)
                        m = (ii - i + 1) * (jj - j + 1)
                        mi, mj, mii, mjj = i, j, ii, jj

    for a in range(mi, mii + 1):
        for b in range(mj, mjj + 1):
            s[a][b] = k


def solve(r, c):
    r, c = int(r), int(c)
    sd = []
    s = [list(input.readline().strip()) for _ in range(r)]
    # print('\n'.join([''.join(ss) for ss in s]))
    # print()
    for i in range(r):
        for j in range(c):
            if s[i][j] != '?' and s[i][j] not in sd:
                find_n_fill(s, s[i][j], r, c)
                sd.append(s[i][j])
    print('\n'.join([''.join(ss) for ss in s]))

for case in range(int(input.readline())):
    s, k = input.readline().split()
    print ("Case #%d:" % (case + 1))
    solve(s, k)
