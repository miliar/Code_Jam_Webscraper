import string, sys

def solve(n, m):
    r = 0
    x = len(str(m))
    while m > n:
        j = n
        while j < m:
            k = 1
            _n = [y for y in str(j)]
            while k < x:
                t = int(''.join(_n[k:]) + ''.join(_n[:k]))
                if t == m:
                    r +=1
                    break
                k += 1
            j += 1
        m -= 1
    return r

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    x = int(f.readline())
    out = open('resultC.out', 'w')
    i = 1
    while x:
        n, m = f.readline().split(" ")
        n = int(n.strip())
        m = int(m.strip())
        print i
        out.write("Case #%d: %s\n" % (i, solve(n, m)))
        x -= 1
        i += 1