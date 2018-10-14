from fractions import gcd

def readnums():
    s = raw_input()
    a = s.split()
    a = [int(x) for x in a]

    if len(a) == 1:
        return a[0]
    return a

def diffs(a):
    res = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                res.append(a[i] - a[j])
            else:
                res.append(a[j] - a[i])
    return res

def gcdn(a):
    r = a[0]
    for i in range(1, len(a)):
        r = gcd(r, a[i])
    return r

def ceiling(x, y):
    if x % y:
        return x / y + 1
    return x / y

def main():
    c = readnums()
    for i in xrange(c):
        t = readnums()[1:]
        g = gcdn(diffs(t))
        ans = ceiling(t[0], g) * g - t[0]
        print 'Case #%d: %d' % (i + 1, ans)
        
if __name__ == '__main__':
    main()
