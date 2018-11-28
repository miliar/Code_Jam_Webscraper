
SI = 'abcdefghijklmnopqrstuvwxyz'
SO = 'ynficwlbkuomxsevzpdrjgthaq'
secret_map = dict(zip(SO, SI))

def solve(s):
    return ''.join(map(lambda x: secret_map.get(x, x), s))

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        res = solve(f.readline().strip())
        print 'Case #%d: %s' % (i + 1, res)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
