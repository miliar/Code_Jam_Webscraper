import sys

fname = sys.argv[1]

def cancollect(r, e):
    k = (r - e) / 2
    return abs(k - e) <= 2

dict = [r for r in range(0,40) for e in range(0,11) if cancollect(r, e)]

def itero(fn):
    with open(fname) as f:
        i = 0
        for line in f:
            if i > 0:
                x = line.strip()
                fn(i, x)
            i += 1

def tst(x, p):
    def i2t(y):
        return (p, (y-p)/2, y - (y-p)/2 - p)
    cA = [i2t(e) for e in [x] if p * 3 - 2 <= e]
    cB = [i2t(e) for e in [x] if p * 3 - 4 <= e < p * 3 - 2]
    return cA, cB

def pro(x):
    N, S, p = x[0:3]
    x = [ e for e in sorted(x[3:], reverse=True)]
    #x = [ e for e in x[3:]]
    def i2t(y):
        px = y /3 if y /3 >= p else p
        return (px, (y-px)/2, y - (y-px)/2 - px)
    def cm(xs):
        return xs[0] >= 0 and xs[1] >= 0 and xs[2] >= 0 \
            and abs(xs[0] - xs[1]) < 2 and abs(xs[0] - xs[2]) < 2 and abs(xs[2] - xs[1]) < 2
    def cmS(xs):
        return xs[0] >= 0 and xs[1] >= 0 and xs[2] >= 0 \
            and all(xs) and (abs(xs[0] - xs[1]) == 2 or abs(xs[0] - xs[2]) == 2 or abs(xs[2] - xs[1]) == 2) \
            and not(abs(xs[0] - xs[1]) > 2 or abs(xs[0] - xs[2]) > 2 or abs(xs[2] - xs[1]) > 2)
    cXs = [(i2t(e)) for e in x]
    cA = filter(cm, cXs) # if p * 3 - 2 <= e])
    cB = filter(cmS, cXs)# if p * 3 - 4 <= e < p * 3 - 2]
    sp = (len(cB)) # if len(cB) <= S else S)
    c = len(cA) + (sp if sp <= S else S)
    return c #, "x='"+str(x) + "'", "S="+str(S), "p="+str(p) , (cA, cB, cXs)


def problemB(i, s):
    r = pro([int(e) for e in s.split()])
    print ("Case #%i:" % i), r


                  
itero(problemB)



