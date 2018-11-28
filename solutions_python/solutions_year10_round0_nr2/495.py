import sys

def gcd(a, b):
    if a < b:
        t = b
        b = a
        a = t
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd2(l):
    g = l[0]
    for a in l[1:]:
        g = gcd(g, a)
    return g

def main():
    input = open(sys.argv[1])
    num = int(input.next())
    
    for i in range(num):
        t = [int(a) for a in input.next().split()][1:]
        dl = [abs(t[j] - t[j+1]) for j in range(len(t)-1)]
        T = gcd2(dl)
        
        for ti in t:
            if ti % T != 0:
                y = T - (t[0] % T)
                break
        else:
            y = 0
        
        print 'Case #%d: %d' % (i + 1, y)
        
if __name__ == '__main__':
    main()
