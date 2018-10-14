from sys import stdin

for case in range(1, int(stdin.readline()) + 1):
    n = int(stdin.readline())
    a = []
    for i in range(n): a.append(stdin.readline().strip())

    wp = [0.0] * n
    owp = [0.0] * n
    oowp = [0.0] * n

    for i in range(n):
        allg = sum(1.0 for j in range(n) if a[i][j] != '.')
        wong = sum(1.0 for j in range(n) if a[i][j] == '1')
        wp[i] = wong/allg

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] != '.':
                cnt += 1
                allg = sum(1.0 for k in range(n) if (a[j][k] != '.' and k != i))
                wong = sum(1.0 for k in range(n) if (a[j][k] == '1' and k != i))
                owp[i] += wong/allg
        owp[i] /= cnt

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] != '.':
                cnt +=1
                oowp[i] += owp[j]
        oowp[i] /= cnt

    print "Case #%d:" % case
    for i in range(n):
        print "%f" % (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])
