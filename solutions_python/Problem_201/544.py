def split(n):
    h = n//2
    return h, n-h-1

def stalls(n):
    Hi, R = split(n), 1
    Lo, r = Hi, 0
    while True:
        yield (Hi,R)
        yield (Lo,r)
        v = Hi[0],Hi[1],Lo[0],Lo[1]
        M, m = max(v), min(v)
        T = 2 * (R + r)
        R = R + (R if Hi[1]==M else 0) + (r if Lo[0]==M else 0) + (r if Lo[1]==M else 0)
        r = T - R
        Hi, Lo = split(M), split(m)


def solve(n, k):
    t = 0
    for Mm, r in stalls(n):
        t += r
        if t >= k:
            return Mm

rd = input

for t in range(1, 1+int(rd())):
    n, k = rd().split()
    M, m = solve(int(n), int(k))
    print('Case #{}: {} {}'.format(t, M, m))
    
