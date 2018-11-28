#!/usr/bin/env python

def padd(x, y):
    a = list(bin(x)[2:])
    b = list(bin(y)[2:])
    
    a.reverse()
    b.reverse()
    
    lena = len(bin(x)) - 2
    lenb = len(bin(y)) - 2
    
    c = []
    for i in xrange(max(lena, lenb)):
        if i < lena and i < lenb:
            n = int(a[i]) ^ int(b[i])
        elif i >= lena:
            n = b[i]
        else:
            n = a[i]
        
        c.append(str(n))
    
    c.reverse()
    return int(''.join(c), 2)



def main():
    cases = input()
    for case in range(1, cases + 1):
        ans = -1
        input()
        line = map(lambda x: int(x), raw_input().split())
        
        for n in xrange(2**len(line)):
            token = [0 for i in xrange(len(line))]
            b = list(bin(n)[2:])
            b.reverse()
            for i in xrange(len(b)):
                token[i] = int(b[i])
            
            x = []
            y = []
            for i in xrange(len(token)):
                if token[i] == 1:
                    x.append(line[i])
                else:
                    y.append(line[i])
            
            l = lambda s, t: padd(s, t)
            l2 = lambda s, t: s + t
            if x and y:
                ga = reduce(l, x)
                gb = reduce(l, y)
                u = reduce(l2, x)
                v = reduce(l2, y)
                if ga == gb:
                    ans = max(ans, u, v)
            
        ans = 'NO' if ans == -1 else ans
        print 'Case #%d: %s' % (case, ans)
    
if __name__ == '__main__':
    main()