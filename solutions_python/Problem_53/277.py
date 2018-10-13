def readnums():
    s = raw_input()
    a = s.split()
    a = [int(x) for x in a]

    if len(a) == 1:
        return a[0]
    return a

def main():
    t = readnums()
    for i in xrange(t):
        n, k = readnums()
        v = 2 ** n
        v1 = v - 1
        if k % v == v1:
            ans = 'ON'
        else:
            ans = 'OFF'

        print 'Case #%d: %s' % (i + 1, ans)
        
if __name__ == '__main__':
    main()
