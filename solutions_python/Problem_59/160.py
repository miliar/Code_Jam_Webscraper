def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r

def parse(path):
    return path.split('/')[1:]

def main():
    t = readInts()[0]
    
    case = 1
    for i in xrange(t):
        n, m = readInts()

        dirs = {}        
        for j in xrange(n):
            p = readString()
            path = parse(p)
            
            pointer = dirs
            for pp in path:
                if not pointer.has_key(pp):
                    pointer[pp] = {}
                pointer = pointer[pp]
        
        count = 0
        for j in xrange(m):
            p = readString()
            path = parse(p)
            
            pointer = dirs
            for pp in path:
                if not pointer.has_key(pp):
                    count += 1
                    pointer[pp] = {}
                pointer = pointer[pp]
        
        print 'Case #%d: %d' % (case, count)
        case += 1

if __name__ == '__main__':
    main()

