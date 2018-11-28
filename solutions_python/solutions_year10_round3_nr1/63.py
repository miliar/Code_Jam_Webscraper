def readInts():
    r = raw_input()
    s = r.split()
    if len(s) == 1:
        return int(s[0])
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r

def main():
    t = readInts()
    
    case = 1
    for i in xrange(t):
        ans = 0
        
        t1 = readInts()
        left = []
        right = []
        for j in xrange(t1):
            a, b = readInts()
            left.append(a)
            right.append(b)
            
        for m in xrange(t1):
            for n in xrange(t1):
                if m == n:
                    pass
                if left[m] < left[n]:
                    if right[m] > right[n]:
                        ans += 1
                else:
                    if right[m] < right[n]:
                        ans += 1
        
        ans /= 2
        
        print 'Case #%d: %d' % (case, ans)
        case += 1

if __name__ == '__main__':
    main()

