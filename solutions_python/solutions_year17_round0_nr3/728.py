def f1(x,y,z):
    x1 = x/2
    if x%2 == 0:
        y1 = y
        z1 = 2*z + y
    else:
        y1 = 2*y + z
        z1 = z
    return x1, y1, z1

def g(N,K):
    k = 1
    x = N
    y = 1
    z = 0
    while k <= K:
        k *= 2
        x,y,z = f1(x,y,z)
    extra = K - k/2 + 1
    if y > z:
        if 2*extra <= y-z:
            return x,x
        else:
            return x,x-1
    if y == z:
        return x,x-1
    if y < z:
        if extra <= y:
            return x,x-1
        else:
            return x-1,x-1
    


with open('in.txt') as f:
    f.readline()
    case = 0
    for line in f:
        case += 1

        line = line.split()
        N = int(line[0])
        K = int(line[1])

        q,w = g(N,K)

        print "Case #%d: %d %d" % (case, q,w)
