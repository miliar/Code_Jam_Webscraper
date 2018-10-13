cases = input()

def calc(v):
    c = 1
    last = v[0]
    for a in v:
        if a != last:
            c += 1
            last = a
    return c

def apply_key(x_old, key):
    x = [ None for x in xrange(len(x_old))]
    for a in xrange(0, len(x_old)- k + 1, k):
        for i in xrange(0, k):
            x[a + i] = s[a + key[i]]
    return x

def bt(v, d_v):
    global orig_size
    if len(v) == orig_size:
        global minim
        if calc(v) < minim:
            return calc(v)
        else:
            return minim
    for i in xrange(len(d_v)):
        d_v3 = list(d_v[i])
        for j in xrange(len(d_v3)):
            v.append(d_v3[i])
            del d_v[i][j]
            bt(v, d_v[1:])
            d_v[i].insert(j, v.pop())

# lista [   [pos1: [] [] [] ],  [pos2: [] []],  ... ]
def comb(x):
    if not x:
        return [[]]
    return [[x[i]] + p for i in range(len(x)) for p in comb(x[:i] + x[i+1:])]

for case in xrange(cases):
    result = 0
    k = input()
    s = raw_input()
    temp = []
    minim = len(s)
    for a in comb(range(k)):
        x = apply_key(s, a)
        tmp = calc(x)
        if tmp < minim:
            minim = tmp
    print 'Case #' + str(case + 1) + ":", minim