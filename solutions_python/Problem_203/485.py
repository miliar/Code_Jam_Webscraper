
def check(cake, mini, maxi, j, ch):
    for i in range(mini, maxi+1):
        if cake[i][j] != '?' and cake[i][j] != ch:
            return False
    return True


def fill(cake, pi, pj):
    mini, maxi = pi, pi
    while mini > 0 and cake[mini - 1][pj] == '?':
        mini -= 1
    while maxi < len(cake)-1 and cake[maxi + 1][pj] == '?':
        maxi += 1
    j = pj
    while j < len(cake[0]):
        if not check(cake, mini, maxi, j, cake[pi][pj]):
            break
        for i in range(mini, maxi+1):
            cake[i][j] = cake[pi][pj]
        j += 1
    j = pj
    while j >= 0:
        if not check(cake, mini, maxi, j, cake[pi][pj]):
            break
        for i in range(mini, maxi+1):
            cake[i][j] = cake[pi][pj]
        j -= 1
    return cake

tests = int(raw_input())
for test in xrange(tests):
    r, c = map(int, raw_input().split())
    cake = []
    for i in xrange(r):
        cake.append(list(raw_input()))
    import copy
    res = copy.deepcopy(cake)
    for i in xrange(c):
        for j in xrange(r):
            if cake[j][i] != '?':
                fill(res, j, i)
    print "Case #{}:".format(test+1)
    for i in xrange(r):
        print "".join(res[i])
