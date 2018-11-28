def read_line(line):
    l = line.split(' ')
    K = int(l[0])
    S = int(l[1])
    return (K,S)

def read_case(f):
    l = f.readline().split(' ')
    D = int(l[0])
    N = int(l[1])
    horses = []
    for i in xrange(N):
        horses += [read_line(f.readline())] 
    return (horses,D)

def read_input(path):
    f = open(path, 'r')
    g = open(path + '_res.txt', 'w')
    T = int(f.readline())
    for i in xrange(T):
        g.write('Case #%d: ' % (i+1))
        h,d = read_case(f)
        s = solve(h,d)
        g.write(s)
    g.close()
    f.close()
    
def solve(horses,d):
    m = 0
    for h in horses:
        t = (d - h[0]) / (1.0 * h[1])
        if t > m:
            m = t
    return str((1.0 * d) / m) + '\n'

read_input('A-large.in')

