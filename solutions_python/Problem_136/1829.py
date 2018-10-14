
def time(c, f, x, m) :
    if m <= 0:
        return x / 2
    else :
        t = 0
        for i in range(m) :
            t += c/(2+i*f)
        t+= x/(2+m*f)
    return t

def solve(f) :
    c, f, x = f.readline().split()
    c = float(c)
    f = float(f)
    x = float(x)
    m = int(x/c - 2/f)
    return time(c, f, x, m)

    

if __name__ == '__main__' :
    with open('B-large.in') as f:
        t = int(f.readline())
        for i in range(t) :
            print ('Case #{0}: {1}'.format(i + 1, solve(f)))
