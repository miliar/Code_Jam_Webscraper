def read_case(line):
    l = line.split(' ')
    p = map(lambda x: (45-ord(x))/2, l[0])
    k = int(l[1])
    return (p,k)

def read_input(path):
    f = open(path, 'r')
    g = open('resA.txt', 'w')
    T = int(f.readline())
    for i in xrange(T):
        line = f.readline()
        g.write('Case #%d: ' % (i+1))
        p,k = read_case(line)
        g.write(solve(p,k))
        g.write('\n')
    g.close()
    f.close()
    
def solve(pancakes, k):
    s = len(pancakes)
    p = pancakes[:]
    res = 0
    for i in xrange(s - k + 1):
        if p[i] == 0:
            res += 1
            for j in xrange(k):
                p[i+j] ^= 1
    if 0 in p:
        return 'IMPOSSIBLE'
    else:
        return str(res)

read_input('A-large.in')
    
