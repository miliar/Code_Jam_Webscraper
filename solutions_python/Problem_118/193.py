try:
    import psyco
    psyco.full()
except ImportError: pass    
from bisect import bisect, bisect_left

def is_pali(n):
    s = str(n)
    l = len(s)
    if l == 1:
        return True
    return s[:l/2] == s[l-1:(l-1)/2:-1] 

P = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]
Z = set(P)

def dfs(s, r, l, n1):
    if l > 26:
        return

    v = int(s + r)
    v2 = v * v
    s2 = str(v2)
    l2 = len(s2)
    if s2[:l2/2] == s2[l2-1:(l2-1)/2:-1]: 
        Z.add(v2)

    v = int(s + '0' + r)
    v2 = v * v
    s2 = str(v2)
    l2 = len(s2)
    if s2[:l2/2] == s2[l2-1:(l2-1)/2:-1]:
        Z.add(v2)
    
    v = int(s + '1' + r)
    v2 = v * v
    s2 = str(v2)
    l2 = len(s2)
    if s2[:l2/2] == s2[l2-1:(l2-1)/2:-1]:
        Z.add(v2)
                
    v = int(s + '2' + r)
    v2 = v * v
    s2 = str(v2)
    l2 = len(s2)
    if s2[:l2/2] == s2[l2-1:(l2-1)/2:-1]:
        Z.add(v2)
    
    dfs(s + '0', '0' + r, l+1, n1)
    if n1 < 4:
        dfs(s + '1', '1' + r, l+1, n1+1)

if __name__ == '__main__':

    fi = open('C.in', 'r')
    fo = open('C.out', 'w')
    T = int(fi.readline().strip('\n\r '))

    dfs('1', '1', 1, 1)
    
    b = '2'
    for i in xrange(27):
        v = int(b + b[::-1])
        if (is_pali(v * v)):
            Z.add(v * v)
        v = int(b + '0' + b[::-1])
        if (is_pali(v * v)):
            Z.add(v * v)
        v = int(b + '1' + b[::-1])
        if (is_pali(v * v)):
            Z.add(v * v)
        b += '0'
        
    #assert 111111111 ** 2 in Z 
    Z = sorted(Z)
    
    for ix in xrange(1, T+1):     
        A, B = fi.readline().strip('\n\r ').split();
        A = int(A); B = int(B)
        ans = (bisect(Z, B)-1) - (bisect_left(Z, A)-1)
        fo.write('Case #%d: %d\n' % (ix, ans))
