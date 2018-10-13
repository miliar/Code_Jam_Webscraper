def main():
    
    id = [1 + 0j, 0 + 0j, 0 + 0j, 1 + 0j]
    mid = [-1 + 0j, 0 + 0j, 0 + 0j, -1 + 0j]
    i = [1j, 0 + 0j, 0 + 0j, -1j]
    j = [0 + 0j, 1 + 0j, -1 + 0j, 0 + 0j]
    k = [0 + 0j, 1j, 1j, 0 + 0j]

    def mult(a, b):
        return [
            a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]
        ]
    
    def sqr(a):
        return mult(a, a)
        
    def pow(a, n):
        if n == 0:
            return id
        if n == 1:
            return a
        if n % 2 == 0:
            return sqr(pow(a, n / 2))
        return mult(a, pow(a, n - 1))
    
    def solve():
        L, X = [int(x) for x in fin.readline().split()]
        s = fin.readline().rstrip('\n')
        
        p = q['1']
        for i in range(len(s)):
            p = mult(p, q[s[i]])
        p = pow(p, X)
        if p != q['-1']:
            return 'NO'
        
        pi = q['1']
        ii = 0
        while ii < min(4, X) * L:
            pi = mult(pi, q[s[ii % L]])
            ii += 1
            if pi == q['i']:
                break
        if pi != q['i']:
            return 'NO'
        
        pj = q['1']
        ij = ii
        while ij < ii + min(4, X) * L:
            pj = mult(pj, q[s[ij % L]])
            ij += 1
            if pj == q['j']:
                break
        if pj != q['j']:
            return 'NO'
        
        return 'YES'
        
        
    q = {
        '1': id,
        'i': i,
        'j': j,
        'k': k,
        '-1': mult(mid, id),
        '-i': mult(mid, i),
        '-j': mult(mid, j),
        '-k': mult(mid, k)
    }
    filename = "c"

    fin = open(filename + ".in", "r")
    fout = open(filename + ".out", "w")

    tests = int(fin.readline())
    for test in range(tests):
        print('Case #%d: %s' % (test + 1, solve()), file=fout)

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()