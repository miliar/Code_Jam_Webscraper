def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def main():
    t = readInts()[0]
    
    case = 1
    for i in xrange(t):
        N, K, B, T = readInts()        
        x = readInts()
        v = readInts()

        passcount = 0
        count = 0
        for j in xrange(len(x) - 1, -1, -1):
            if T * v[j] + x[j] >= B:
                passcount += 1
                if passcount >= K:
                    break
            else:
                count += K - passcount

        if passcount < K:
            print 'Case #%d: IMPOSSIBLE' % (case)
        else:
            print 'Case #%d: %d' % (case, count)
        case += 1

if __name__ == '__main__':
    main()

