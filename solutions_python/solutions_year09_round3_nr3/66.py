frac = [0 for _ in range(10)]
frac[1]=1
for i in range(2, 10):
    frac[i] = frac[i-1]*i

def perm(k, g):
    s = g[:]
    kk = k
    for j in range(2, len(s)):
        tmp = s[kk%j+1]
        s[kk%j+1] = s[j]
        s[j] = tmp
        kk = kk // j
    return s

def aperm(s):
    n = frac[len(s)]
    r = [s]
    for i in range(1,n):
        print(i)
        r.append(perm(i, r[-1]))
    return r

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

        
def bCell(cell, p):
    if p==cell[0] and p==cell[1]:
        return []
    elif p==cell[0]:
        return [(p+1, cell[1])]
    elif p==cell[1]:
        return [(cell[0], p-1)]
    return [(cell[0], p-1), (p+1, cell[1])]

def sCells(cell, ps):
    sum_m = 0
    cs = [cell]
    for s in ps:
        tc = None
        for cc in cs:
            if cc[0]<=s and cc[1]>=s:
                tc = cc
                break
        if tc is not None:
            cs.remove(tc)
            bs = bCell(tc, s)
            cs.extend(bs)
            for bbs in bs:
                sum_m = sum_m + (bbs[1]-bbs[0]+1)
    return sum_m


def solve(P, Q):
    ans = -1
    for comb in all_perms(Q):
        s = sCells((1,P), comb)
        if ans==-1 or s<ans:
            ans = s
    return ans


fin = open('C-small-attempt0.in')
fout = open('out.txt', 'w')
N = int(fin.readline())
for i in range(1, N+1):
    P, q = [int(x) for x in fin.readline().split()]
    Q = [int(x) for x in fin.readline().split()]
    
    ans = solve(P,Q)
    result = 'Case #%d: %d'%(i, ans)
    print(result)
    fout.write(result+'\n')

fin.close()
fout.close()
