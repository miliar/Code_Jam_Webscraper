def solve(d,n,K,S):
    last_t = 0
    for i in range(len(K)):
        k,s = K[i],S[i]
        t_to_finish = (d-k) * 1.0 / s
        last_t = max(last_t, t_to_finish)
    return d / last_t

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        d,n = map(int,r.readline().split())
        K,S=[],[]
        for a0 in range(n):
            k,s = map(int,r.readline().split())
            K.append(k)
            S.append(s)
        w.write('Case #{0}: {1}\n'.format(case, solve(d,n,K,S)))
        
