import os
import itertools


def permutations(packs,p):
    g = itertools.permutations([i for i in xrange(p)])
    p1 = packs[0]
    p2 = packs[1]
    res = []
    for x in g:
        y = [p2[i] for i in x]
        res.append([p1,y])
    return res

def gma(x, a):
    g = 1.*x/(0.9*a)
    s = max(0, int(g) - 10)
    while s * a * 90 <= 100 * x:
        s += 1
    return s - 1

def gmi(x, a):
    g = 1.*x/(1.1*a)
    s = int(g) + 10
    while s * a * 110 >= 100 * x:
        s -= 1
    return s + 1

def mima(b,a):
    mi = max(0, 100*b/(110*a) - 5)
    ma = 100*b/(90*a) + 6
    gmi = 10**9
    gma = 0
    for i in xrange(mi,ma):
        if i*a*90 <= b*100 <= i*a*110:
            gmi = min(gmi, i)
            gma = max(gma, i)
    return gmi, gma


def check(packs, ingredients, n):
    ma = 0
    mi = 10**9
    for i in xrange(n):
        g = gma(packs[i],ingredients[i])
        mi = min(mi, g)
        g = gmi(packs[i], ingredients[i])
        ma = max(ma, g)

    return mi > 0 and ma <= mi

def check2(b1,a1,b2,a2):
    mi = max(0, 100 * b1 / (110 * a1) - 5)
    ma = 100 * b1 / (90 * a1) + 6
    gmi = 10 ** 9
    gma = 0
    for i in xrange(mi, ma):
        if i * a1 * 90 <= b1 * 100 <= i * a1 * 110 and i * a2 * 90 <= b2 * 100 <= i * a2 * 110:
            return True
    return False

def nk(perm, ingredients, p, n):
    c = 0
    for i in xrange(p):
        packs = [perm[j][i] for j in xrange(n)]
        b1,b2 = packs
        a1,a2 = ingredients
        if check2(b1,a1,b2,a2):
            c += 1
        # if check(packs, ingredients, n):
        #     c += 1
    return c

def solve1(packs,b,p):
    c = 0
    for i in xrange(p):
        a = packs[i]
        mi,ma = mima(a,b)
        if ma > 0 or mi < 10**9:
            c += 1
    return c

def solve(n, p, packs, ingredients):
    if n == 1:
        return solve1(packs[0], ingredients[0], p)
    if n > 2: return 0
    ma = 0
    for perm in permutations(packs,p):
        g = nk(perm, ingredients, p, n)
        ma = max(ma,g)
    return ma

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1A/B.in")) as f:
    m = int(f.readline().strip('\n'))
    print m
    for i in range(m):
        n,p = [int(x) for x in f.readline().strip().split(' ')]
        ingredients = [int(x) for x in f.readline().strip().split(' ')]
        pack = []
        for j in xrange(n):
            row = [int(x) for x in f.readline().strip().split(' ')]
            pack.append(row)
        res = solve(n, p, pack, ingredients)
        print 'Case #' + str(i + 1) + ': ' + str(res)