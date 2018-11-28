def mult(a, b):
    if a == '1':
        return b
    if b == '1':
        return a
    if a == b:
        return '-1'
    if '-' in a or '-' in b:
        sign = 1
        if '-' in a:
            sign *= -1
        if '-' in b:
            sign *= -1
        if sign == 1:
            return mult(a[1], b[1])
        else:
            partial = mult(a[-1], b[-1])
            return '-' + partial if '-' not in partial else partial[1]
    d = {
         ('i', 'j') : 'k',
         ('i', 'k') : '-j',
         ('j', 'i') : '-k',
         ('j', 'k') : 'i',
         ('k', 'i') : 'j',
         ('k', 'j') : '-i'
         }
    
    return d[(a,b)]

def solve(s, X, target):
    full = s * X
    i = 0
    for j, piece in enumerate(target):
        if i >= len(full): return "NO"
        val = full[i]
        i += 1
        while val != piece and i < len(full):
            val = mult(val, full[i])
            i += 1
    if i == len(full):
        return "YES"
    base = '1'
    for factor in full[i:]:
        base = mult(base, factor)
    if base == '1': 
        return "YES"
    return "NO"
    

fin = open("C-small-attempt0.in.txt")
fout = open("C.out", "w")
T = int(fin.readline().strip())

for i in range(T):
    L, X = map(int, fin.readline().strip().split())
    s = fin.readline().strip()
    ans = solve(s, X, 'ijk')
    fout.write("Case #{}: {}\n".format(i+1, ans))
