import math

def find_range(num, base):
    lower = math.ceil(num/(base*1.1))
    upper = math.floor(num/(base*0.9))
    if lower > upper:
        return None
    else:
        return (lower, upper)

for saddsgfg in range(int(input())):
    n, p = map(int, input().split())
    req = list(map(int, input().split()))
    L = []
    for i in range(n):
        inp = map(int, input().split())
        inp = [find_range(x, req[i]) for x in inp]
        L.append([x for x in inp if x is not None])
        
    if n == 1:
        ans = len(L[0])
    elif n == 2:
        possib = set()
        n1 = len(L[0])
        n2 = len(L[1])
        for a in range(n1):
            aele = L[0][a]
            for b in range(n2):
                bele = L[1][b]
                if max(bele[0], aele[0]) <= min(bele[1], aele[1]):
                    possib.add((a, b))
        getpossib = lambda x: [y for y in range(n2) if (x, y) in possib]
        maxset = set()
        hashset = set()
        def xpand(taken, ind):
            if ind >= n1:
                maxset.add(len(taken))
                return None
            if (taken, ind) in hashset:
                return
            xpand(taken, ind + 1)
            for y in [y for y in getpossib(ind) if y not in taken]:
                xpand(taken + (y,), ind + 1)
            hashset.add((taken, ind))
        xpand((), 0)
        ans = max(maxset, default = 0)
            
    print('Case #{}: {}'.format(saddsgfg+1, ans))
