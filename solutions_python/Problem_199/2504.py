def solve(s,k):
    if all(map(lambda x: x == '+',s)):
        return 0
    else:
        t = [c for c in s]
        res = 0
        while '-' in t and res <= len(s):
            i = t.index('-')
            res = res + 1
            for j in range(i,i+k):
                try:
                    if t[j]=='-':
                        t[j]='+'
                    else:
                        t[j]='-'
                except IndexError:
                    return 'IMPOSSIBLE'
    if res > len(s):
        return 'IMPOSSIBLE'
    return res
with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        s,k = r.readline().split()
        k = int(k)
        w.write('Case #{0}: {1}\n'.format(case, solve(s,k)))
        
