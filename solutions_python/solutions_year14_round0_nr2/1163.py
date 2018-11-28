filename = 'B-large.in' #raw_input()

def solve(param):
    c = float(param[0])
    f = float(param[1])
    x = float(param[2])
    r = 2.
    res = 0.
    while True:
        if x/r <= x/(r+f) + c/r :
            break
        res += c/r
        r += f
    res += x/r
    return res

with open (filename) as f:
    T = int(f.readline())
    for icase in range(T):
        param = f.readline().split()
        print 'Case #%s: %s' % (icase+1 ,solve(param))

