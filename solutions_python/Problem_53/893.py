def load_file(fname):
    f = open(fname)
    count = int(f.readline())
    i = 0
    while i < count:
        i += 1
        n,k = [int(x) for x in f.readline().split(' ')]
        print 'Case #%d: %s' % (i, 'ON' if k&(2**n-1) == 2**n-1 else 'OFF')

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print 'missing datefile parameter'
        sys.exit()
    else:
        load_file(sys.argv[1])
