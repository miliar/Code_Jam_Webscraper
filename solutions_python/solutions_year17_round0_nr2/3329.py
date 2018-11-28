def isTidy(x):
    p = x % 10
    while x > 0:
        x = x // 10
        c = x % 10
        if c > p or (c == 0 and x > 0):
            return False
        p = c
    return True

def nextX(x):
    e = 1
    p = x
    r = 0
    
    while p > 0:
        q = p % 10
        if q == 0:
            break
        else:
            e *= 10
            p = x // e
            r = x % e
    
    if p == 0:
        return x - 1
    else:
        return x - r - 1

fi = open('B-small-attempt0.in', 'r')
fo = open('outputB-small.txt', 'w')

T = int(fi.readline())

for t in range(T):

    X = int(fi.readline())
    
    tidy = False
    while True:
        tidy = isTidy(X)
        if tidy:
            break
        X = nextX(X)
        
    print('Case #{0}: {1}'.format(t+1, X))
    fo.write('Case #{0}: {1}\n'.format(t+1, X))
    
fi.close()
fo.close()

