import sys


def stodigits(s):
    return [int(c) for c in s]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        quit()

    fname = sys.argv[1]
    data = ''

    try:
        infile = open(fname)
        outfile = open('unitblarge.out', 'w')
        T = int(infile.readline().strip())

        for t in range(1, T+1):
            s = infile.readline().strip()
            digs = stodigits(s)
            for i in range(0, len(digs) - 1):
                if digs[i] > digs[i+1]:
                    j = i
                    while j > 0 and digs[j - 1] == digs[i]:
                        j -= 1
                    digs[j] -= 1
                    for n in range(j + 1, len(digs)):
                        digs[n] = 9
            while digs[0] == 0 and len(digs) > 1:
                del digs[0]
            res = 'Case #%d: %s' % (t, ''.join(map(str, digs)))
            print res
            outfile.write(res)
            outfile.write('\n')
        outfile.close()
        infile.close()
    except Exception as e:
        print 'Read error:', e
        quit()

    
