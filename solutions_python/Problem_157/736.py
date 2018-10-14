m = [[0,0,0,0,0],[0,1,2,3,4],[0,2,-1,4,-3],[0,3,-4,-1,2],[0,4,3,-2,-1]]

def multi(a, b):
    if a*b > 0:
        sig = 1
    else:
        sig = -1
    return sig * m[abs(a)][abs(b)]

m2d = {'i':2, 'j':3, 'k': 4}

def find(start, s, e, X):
    i = start 
    cur = 1
    ls = len(s)
    while i < X*ls:
        cur = multi(cur, m2d[s[i%ls]])
        if cur == e:
            return i
        i += 1
    return -1

def calc(L, X, s):
    pos_of_i = find(0, s, 2, X)
    if pos_of_i == -1:
        return False
    pos_of_j = find(pos_of_i + 1, s, 3, X)
    if pos_of_j == -1:
        return False
    pos_of_k = find(pos_of_j + 1, s, 4, X)
    if pos_of_k == -1:
        return False
    one = 1
    i = pos_of_k +1
    while i < L*X:
        one = multi(one, m2d[s[i%L]])
        i += 1
    return one == 1

T = int(raw_input())
for t in range(1, T+1):
    line = raw_input()
    L, X = [int(x) for x in line.split(' ')]
    s = raw_input()
    if calc(L, X, s):
        print "Case #%d: YES" % t
    else:
        print "Case #%d: NO" % t
