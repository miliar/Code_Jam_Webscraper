from collections import defaultdict

def solve(X,S,R,t,ws):
    remain = defaultdict(int)
    for s,e,w in ws:
        remain[w] += e-s
    X -= sum(remain.values())
    if X: remain[0] += X

    est = 0
    while remain:
        w = min(remain)
        if t > 0:
            distance = t * (R+w)
            if distance < remain[w]:
                est += t
                remain[w] -= distance
                t = 0
            else:
                ti = remain[w] / float(R+w)
                est += ti
                t -= ti
                del remain[w]
        else:
            est += remain[w] / float(S+w)
            del remain[w]
    return est

if __name__ == '__main__':
    import sys
    rl = iter(sys.stdin).next
    T = int(rl())
    for i in range(1,T+1):
        X,S,R,t,N = map(int, rl().split())
        ws = [map(int, rl().split()) for _ in range(N)]
        print 'Case #{}: {}'.format(i, solve(X,S,R,t,ws))
