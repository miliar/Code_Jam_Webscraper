def add(g,d):
    ds = d.split('/')
    for i in range(len(ds)):
        path = '/'.join(ds[0:i+1])
        g.append(path)
    return(g)

def check(g, d):
    ds = d.split('/')
    new = 0
    for i in range(len(ds)):
        path = '/'.join(ds[0:i+1])
        if not (path in g):
            new = new+1
    return(new)     



if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    #in_file = 'test.txt'
    #out_file = 'out1.txt'

    lines = open(in_file).readlines()
    lines = lines[1:]
    case = 0

    wfile = open(out_file, 'w')

    while lines:
        case += 1
        m, n = lines[0].strip().split()
        m = int(m); n = int(n);

        lines = lines[1:]
        old = lines[:m]
        lines = lines[m:]
        new = lines[:n]
        lines = lines[n:]
        g = list()

        for line in old:
            line = line[1:]
            line = line.strip()
            g = add(g, line)

        s = 0
        for line in new:
            line = line[1:]
            line = line.strip()
            s += check(g, line)
            g = add(g, line)

        wfile.write('Case #' + str(case) + ': ')
        wfile.write(str(s) + '\n')

        #lines = lines[(m+n):]

    wfile.close()

