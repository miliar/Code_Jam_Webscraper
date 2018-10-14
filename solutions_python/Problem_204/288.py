import math
t = int(raw_input())

def intersect(r1, r2):
    valid_range = r1
    dbound, ubound = r2
    if (valid_range[0] <= dbound <= valid_range[1]):
        return True
    if dbound < valid_range[0] and ubound >= valid_range[0]:
        return True
    return False

searched = set()
result = []

def dfs(pj, r):
    global n, ing, searched, result, p
    if r == n-1: return True
    for j in xrange(p):
        if intersect(ing[r][pj], ing[r+1][j]) and (r+1, j) not in searched:
            searched.add((r+1, j))
            if result[r+1][j] == -1 or dfs(j, r+1):
                result[r+1][j] = pj
                return True
    return False
    
for a in xrange(t):
    [n, p] = [int(_) for _ in raw_input().replace('\r','').split(' ')]
    serve = [int(_) for _ in raw_input().replace('\r','').split(' ')]
    res = 0
    result = [[-1 for c in xrange(p)] for r in xrange(n)]
    ing = [[] for _ in xrange(n)]
    for j in xrange(n):
        q = [int(_) for _ in raw_input().replace('\r','').split(' ')]
        q = [(math.ceil(i/1.1/serve[j]), math.floor(i/0.9/serve[j])) for i in q]
        ing[j] = [i if i[0] <= i[1] else (-1, -2) for i in q]
    for j in xrange(p):
        searched = set()
        if ing[0][j][0] <= ing[0][j][1] and dfs(j, 0): res += 1
    print 'Case #%d: %d' % (a+1, res)
    