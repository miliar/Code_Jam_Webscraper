
def fillback(mat, r, start, ch, docol=False):
    for i in xrange(start, -1, -1):
        if not docol:
            if mat[r][i] == '?':
                mat[r][i] = ch
            else:
                return
        else:
            if mat[i][r] == '?':
                mat[i][r] = ch
            else:
                return


def fillfront(mat, r, c, start, ch, docol=False):
    i = start
    for i in xrange(start, c):
        if not docol:
            if mat[r][i] == '?':
                mat[r][i] = ch
            else:
                break
        else:
            if mat[i][r] == '?':
                mat[i][r] = ch
            else:
                break
    return i

def findsize(mat, r, c, docol=False):
    for i in xrange(r):
        j = 0
        while j < c:
            if not docol:
                val = mat[i][j]
            else:
                val = mat[j][i]
            if val != '?':
                fillback(mat, i, j - 1, val, docol)
                j = fillfront(mat, i, c, j + 1, val, docol)
            else:
                j += 1




if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for case in xrange(1, t + 1):
        r, c = [int(x) for x in raw_input().split(' ')]
        mat = [[0] * c for _ in xrange(r)]
        for i in xrange(r):
            s = raw_input()
            for j in xrange(c):
                mat[i][j] = s[j]
        findsize(mat, r, c)
        findsize(mat, c, r, docol=True)
        print "Case #{}:".format(case)
        for i in xrange(r):
            print ''.join(mat[i])
