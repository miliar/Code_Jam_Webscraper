#!/usr/bin/python

def wp(i, mat, N, ar = None):
    if not ar:
        ar = []

    total = 0
    won = 0
    for j in range(0, N):
        if j in ar:
            continue
        if not mat[i][j] == '.':
            total += 1
        if mat[i][j] == '1':
            won += 1

    return won * 1.0 / total

def owp(i, mat, N):
    res = 0.0
    cnt = 0
    for j in range(0, N):
        if not mat[i][j] == '.':
            res += wp(j, mat, N, [i])
            cnt += 1
    return res / cnt

def oowp(idx, mat, N):
    res = 0.0
    cnt = 0
    for j in range(0, N):
        if not mat[i][j] == '.':
            res += owp(j, mat, N)
            cnt += 1
    return res / cnt

if __name__ == '__main__':
    T = int(raw_input())
    for k in range(0, T):
        N = int(raw_input())
        mat = []
        for i in range(0, N):
            row = raw_input()
            mat.append([])
            for j in row:
                mat[i].append(j)
        print 'Case #' + str(k+1) + ':'
        for i in range(0, N):
            # print wp(i, mat, N), owp(i, mat, N), oowp(i, mat, N)
            print '%.20f' % (.25*wp(i, mat, N) + .5*owp(i, mat, N) + .25*oowp(i, mat, N))

